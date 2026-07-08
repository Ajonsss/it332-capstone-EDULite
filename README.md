# it332-capstone-EDULite

  # Important Dates to Remember:
  June 17, 2026 - Creation of GitHub repository.

  July 2026 - (To follow)

  August 2026 - (To follow)

  # Milestones Per Week
  1. User login and authentication
  2. Creation of student accounts
  3. Importing of student records through excel files
  4. Data Analytics Processes
  5. Integration of Artificial Intelligence in the system

# Lab Activity

# Week 1 - Deliverable
  Lab Activity 1: Week 1 Deliverable 
  
  1. List all systems/APls your capstone might integrate with
  
  One of the few possible APIs that our capstone might integrate with is the Gemini API. Aside from being a capstone requirement, this will also help aid in the creation of the prescriptive analytics report.
  
  2. For each: what data, what direction, how often?
  
  Gemini API
  
  Data: Student Scores
  
  The data that is necessary for the API exchange is the students' scores. This will determine the performance analytics of the students and will be used by the API for the other types of analytics present in the system.

  Direction: Two-way (Capstone System ↔ Gemini API)
  
  How often: The data exchange will be in-demand, whenever the user requests analytics, reports, or the produced recommendations.
  
  4. Create GitHub repo: it332-capstone-groupname
  
  5. Add all members + instructor as collaborators
  
  6. Create README.md with your integration audit
  
  7. Push + create PR: "Week 1 - Integration Audit"

# Discussion of possible changes (June 17, 2026 Discussion)
- Possible switch to the use of Python in the system
- Possible scheduling of environment assessment for Wi-Fi coverage in school
- Switching from Web App to Desktop App
- Discussion of changes in importing of student scores from QR scanner to importing xlsx files.

# Think about YOUR capstone system:
Does your system need to talk to other systems?
- No, it is a stand-alone system.

Does your system need external data?
- Yes, we need the data of students score for analytics to access their performance.

Does your system need export/import?
- Yes, our system need export/import for excel files that has student scores.

Does your system need automation?
- Yes, We will be using the Google Gemini API for generation of analytics report.

# Database Schema (Additional Notes)
- Login
  - email
  - password
- Students
  - id
  - StudentName
  - Scores

# Week 2 - Deliverable
Task for Tuesday (June 30, 2026)
  - Ability to create, delete and edit student accounts
  - Student accounts should include student's name and score

Reflection from previous week's deliverables and code:
  -The login and registration system has been succesfully implemented, but no user interface has been created yet.

  # Front-End primary research for 8-bit pixel type style:
 - Frontend Integration Process

1. Define the Project Structure

Organize the project into separate components:

- Backend – Application logic and data processing.
- Frontend – User interface, rendering, and input handling.
- Assets – PNG sprites, UI elements, fonts, and audio.

---

2. Frontend Framework (Pygame)

Framework: Pygame

Pygame will serve as the application's frontend engine. It is responsible for:

- Rendering custom 8-bit PNG graphics.
- Handling keyboard and mouse input.
- Managing the application window.
- Playing animations and audio.
- Updating the screen every frame.

All interface elements (buttons, menus, icons, backgrounds, etc.) will be created using our own pixel-art assets.

---

3. Organize Assets

Store all visual resources in a dedicated `assets/` folder.

Example:

```text
assets/
├── sprites/
├── ui/
├── icons/
├── fonts/
└── audio/
```

---

4. Load Assets

Use an Asset Manager to load images, fonts, and audio once during startup. Loaded assets are reused throughout the application to improve performance.

---

5. Build the User Interface

Design the application's screens and reusable UI components, such as:

- Main Menu
- Settings
- Buttons
- Panels
- Dialog Boxes

---

6. Render the Interface

For each frame, the frontend will:

1. Clear the screen.
2. Draw the background.
3. Draw UI components.
4. Draw sprites and animations.
5. Update the display.

---

7. Handle User Input

Capture keyboard and mouse events, then send the appropriate actions to the backend.

---

8. Connect Frontend and Backend

The frontend displays information, while the backend processes application logic. User actions trigger backend functions, and the frontend refreshes the interface to reflect any changes.

---

9. Test and Optimize

Before release:

- Test all UI screens.
- Verify asset loading.
- Check performance and animations.
- Package the application for distribution.

---

# Week 3 - Deliverable
- (To follow)

# 07/06/26 
- Presented our current progress on our capstone project.
- For the finals, we are required to present the completed capstone project to our client.

# 07/08/26
- Consulted our thesis adviser and panel regarding potential revisions to our research objectives.
- Discussed and received feedback on the proposed changes to the project's scope and direction.
- Possible change to the technology stack that will be used.
- Considered shifting the application platform from a desktop application to a web application.

