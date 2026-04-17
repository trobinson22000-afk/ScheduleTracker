# ScheduleTracker

- Schedule tracker I built to handle schedule data at work. For obvious reasons, actual schedule data is not included. However, I did include the template used so it can be translated/swapped for other schedules to be tracked.

- The tracker is built to handle data for production jobs and separate all jobs by date, materials, and tools required to produce each job. It compiles this information separated by machines and displays it in easy to read graphs.

- FUTURE GOALS -
- Edit graphs to also display Amount of dies/materials (Displays more in depth information to improve time estimations)
- Add the ability to modify job data from within the panel. (Allows schedules to be modified without editing the csv, and regenerating the entire panel)
- Add API calls to automate the process with the current schedule system (Will not commit this update online, the moment I create this update this project will remain stagnant on gitHub for security reasons)
- Add notifiers to display whether material/tools are on hand to allow maximum response time ahead of due dates
- Customizable colors for the panel
- Restructure the panel to allow it to run on cloud environments. I would like to build this panel to be utilized via private Azure services to remove the single computer restriction the current version has
