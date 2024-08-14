# Implement Screen Sharing in a WebRTC Application

## Objective

The goal of this task is to enhance an existing WebRTC application by adding a screen sharing feature, allowing users to share their screen with other participants in a video call.

## Task Description

You will be provided with a sample WebRTC application hosted on GitHub. Your task is to implement the screen sharing functionality using the WebRTC APIs.

## Steps to Complete the Task

1. **Clone the Repository**  
   Start by cloning the provided GitHub repository containing a basic WebRTC video call application.

2. **Understand the Existing Code**  
   Familiarize yourself with the existing codebase, focusing on how video and audio streams are established between peers.

3. **Implement Screen Sharing**
   - Use the `getDisplayMedia()` API to capture the screen.
   - Modify the existing peer connection to include the screen stream.
   - Ensure that the shared screen is sent to the remote peer and displayed in the application.

4. **UI Updates**
   - Update the user interface to include a button for starting and stopping screen sharing.
   - Ensure that the application can switch seamlessly between camera and screen sharing.

5. **Testing**
   - Test the implementation to ensure screen sharing works correctly across different browsers and devices.

## Requirements

- **Input:** A sample WebRTC application repository (provided).
- **Output:** An enhanced version of the application with functional screen sharing capabilities.

## Technical Specifications

- **Language:** JavaScript (for the front-end).
- **Libraries:** Utilize WebRTC APIs and any additional libraries used in the provided repository.
- **Error Handling:** Implement error handling for screen sharing permissions and peer connection issues.
- **Documentation:** Provide comments in the code and update this README file to include instructions on how to use the new screen sharing feature.

## Sample Repository

You can use the following sample repository as a starting point for your implementation:
- [WebRTC Video Call Example](https://github.com/webrtc/samples/tree/gh-pages/src/content/getusermedia)

## Evaluation Criteria

- **Functionality:** The screen sharing feature should work correctly and be easy to use.
- **Code Quality:** The code should be well-organized, readable, and properly commented.
- **User Experience:** The UI should be intuitive, allowing users to easily start and stop screen sharing.
