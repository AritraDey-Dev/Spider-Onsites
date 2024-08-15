import { io } from "../index.js";
import Auction from "../models/auction.model.js";
import Bid from "../models/bid.model.js";

export const socketIoConnectioin = () => {
  let users = [];

  io.on("connection", (socket) => {
    console.log("a user connected");

    socket.on("joinAuction", (userId) => {
      socket.join(userId); 

      const user = users.find((user) => user.userId === userId);
      if (!user) {
        users.push({ userId, socketId: socket.id });
      } else {
        user.socketId = socket.id;
      }
      console.log(users);
    });

    socket.on("newBid", (data) => {
    
      console.log(data, "new bid data............");

      console.log(users, "users...........,,,,,,,,,new bide data.");
      users.forEach((user) => {
        io.to(user.socketId).emit("newBidData", data);
      });
    });


    socket.on("sendNewBidNotification", async (data) => {

      const auctionData = await Auction.findById(data.auctionId);
      if (!auctionData) {
        return;
      }

      if (data.type === "BID_PLACED") {
        var notification = {
          user: null,
          message: `${data.fullName} has placed a ${data.newBidAmount}$ bid on ${auctionData?.name}`,
          type: "BID_PLACED",
          auction: data.auctionId,
          link: `/single-auction-detail/${data.auctionId}`,
        };
      }


      users.forEach((user) => {
        notification.message = `${
          data.id === user.userId ? "you" : data.fullName
        } placed a ${data.newBidAmount}$ bid on  ${auctionData?.name}`;

        io.to(user.socketId).emit("newBidNotification", notification);
      });
    });

    socket.on("selectWinner", async (id) => {
    

      const bids = await Bid.find({ auction: id });
      console.log(bids, "auction.........");
      if(bids.length === 0){
       return users.forEach((user) => {
          io.to(user.socketId).emit("winnerSelected", null);
        });
      }
      
      let maxBidId = bids[0]._id;
      let maxAmount = bids[0].bidAmount;
      for (let i = 1; i < bids.length; i++) {
        if (bids[i].bidAmount > maxAmount) {
          maxAmount = bids[i].bidAmount;
          maxBidId = bids[i]._id;
        }
      }

      console.log(maxAmount, "maxAmount");
      console.log(maxBidId, "maxBid");
      const auction = await Auction.findById(id);
      const winnerUser = await Bid.findById(maxBidId).populate(
        "bidder",
        "fullName email phone profilePicture"
      );

      console.log(winnerUser, "winnerUser,,,,,,,,,,,,,,,,,lllllll");

      auction.winner = maxBidId;
      auction.status = "over";

      await auction.save();


      users.forEach((user) => {
        io.to(user.socketId).emit("winnerSelected", winnerUser);
      });
    });

    socket.on("disconnect", () => {
      console.log("user disconnected");
    
      users = users.filter((user) => user.socketId !== socket.id);
    });
  });
};
