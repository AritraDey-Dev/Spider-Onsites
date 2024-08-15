# Chess Game with Multiplayer and Rating System

## Features

### User Authentication and Management:

- **Sign Up and Login:** Allow users to create accounts and log in securely.
- **User Profiles:** Display user information and statistics, including their rating.
- **Authentication:** Use JWT for secure authentication.

### Chess Game Functionality:

- **Real-Time Multiplayer:** Enable users to play chess games in real-time against each other.
- **Chessboard Interface:** Implement a graphical chessboard where players can see the current game state.
- **Legal Moves:** Implement legal move validation for all chess pieces, including special moves like castling and en passant.

### Multiplayer Features:

- **Create and Join Matches:** Users can create new matches or join existing ones from a lobby interface.
- **Real-Time Updates:** Use WebSockets to ensure real-time updates of game state between players.
- **Turn-Based Play:** Manage turns and move validation between players, ensuring fair gameplay.

### Rating System:

- **Elo Rating System:** Implement a rating system to calculate and display player ratings based on match outcomes.
- **Rating Updates:** Adjust player ratings after each game based on wins, losses, or draws.
- **Leaderboard:** Display a leaderboard of top-rated players based on Elo rating.

### User Interface:

- **Responsive Design:** Ensure the application is responsive and works well on different devices.
- **Game Controls:** Provide intuitive controls for players to make moves and interact with the chessboard.
- **Lobby Management:** Allow players to see active matches, join games, and view player profiles.
