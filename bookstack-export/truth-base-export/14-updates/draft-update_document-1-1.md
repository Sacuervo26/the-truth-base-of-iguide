Draft Update
Draft Update
A “Draft Update” is a change to the initial iGUIDE visually or cosmetically. A Draft
update is typically one of two things:
A Pano Update is when an operator has returned to a property to
re-document/re-shoot specific areas of a floor because something has changed (Eg.
new paint, different time of year, etc.). The operator would then create a Draft Update
task for the Drafting Team to add the new scans containing the new visual data.
A Floor Plan Update is when an operator has returned to a property to
re-document/re-shoot or scan additional areas of a floor because something has
changed structurally or there was a missing area/floor/building. (Eg. Missing Closet,
Missing Basement, Missing Detached Garage, Full Remodel, Demolition, etc.). The
operator would then create a Draft Update task for the Drafting Team to add the new
scans containing new visual data in conjunction with new laser data capturing new or
more structure to draft.
Draft Updates unfortunately use Full/Original Data only. Light Data is not and cannot
be used to perform a Draft Update.
*This is on R&D’s Roadmap to allow us to use Light Data.

A Draft Update will appear in the QA Queue with the following Badge:

Figure #1 - Draft Update, Work Order/Task

1

Draft Update Procedure (Pano Update)
The procedure at a glance is to download the published iGUIDE, download the new
stitch data, merge the new stitch data into the published file, replace the panos (insert
new, deactivate old) then reupload the project back to the Portal.
1) While in the QA Queue, select the blue “claim next work order” button.

Figure #2 - Claim Next Work Order

2) The Task Details Page will open with the Quality Technician as the claimer listed
under the QA section. No name will be listed under the Drafter section as there
is no Draft to QA workflow for updates.
a) The Description field will indicate what is involved with the update.
b) The Description field for this example indicates that the operator would
like us to process this as a Pano Update.
*Note: Some descriptions are very thorough, others are not so some investigation
may be required.
3) Download or open any additional images of the work order (task) located within
the Supporting Documents section if available.

2

Figure #3 - Task Details Page//Update Request

Figure #4 - Work Order is Claimed by the Quality Technician

3

4) Scroll down to the “Stitch Data” section. Click on the blue “Download Original
Stitch Data” button. This will download the operator's new additional panos
(scans) to be added to the initial iGUIDE.

Figure #5 - Stitch Data: Download Original Stitch Data

5) Scroll down further on the Task Details Page to the “Published Draft Data”
section and click the “Download published Draft data” button. This will download
the initial published iGUIDE data.
*Note: For an update involving an iGUIDE that is in pre-published state, this section
will be displayed as “Pre-published Draft Data” and the blue button will read,
“Download pre-published Draft data”.

Figure #6 - Published Draft Data: Download Published Draft Data

4

a) The Initial iGUIDE will appear with the “draft.tar” file extension within the
downloads folder. The new data to be added will appear with the
“orig-stitch-data.tar” file extension.

Figure #7 - Downloads Folder: draft.tar (old) & orig-stitch-data.tar (new)

6) Once both sets of data have been downloaded, open the Initial iGUIDE (draft.tar)
using Draft.

Figure #8 - Select the draft.tar to Open in Draft First

5

7) Once the Initial draft.tar has been opened within Draft, right-click the property
address within the Project Explorer, click “Merge with Existing Project” and select
the file with the “orig-stitch-data.tar” file extension.

Figure #9 - Merge with Existing Project

6

Figure #10 - Select the orig-stitch-data.tar to Merge

8) AI Processing will begin and last anywhere from less than a minute to upwards
of an hour depending on the size of the update.
*This is on R&D’s Roadmap to have AI processing happen on the Portal as opposed to Draft.

Figure #11 - Waiting to Finish AI Background Processing

7

9) Once AI processing is complete and the two sets of data have been merged into
one, the new data will appear as a New Building with associated floor(s) within
the Project Explorer.

Figure #12 - New Data Will Appear as a New Main Building

8

10)Right-Click the floor(s) of the new data set and select “Add Asterisk to Scan
Names”. This will show in future that an update was performed on this property.
It also helps keep track of the new data when placing it on the same floor as the
old data.

Figure #13 - Add Asterisk to Scan Names

9

11) Once new scans have been identified and received an appended asterisk, select
and drag them to the appropriate floor.
a) Left-click on the first scan within the project explorer and while holding
shift select the last scan. Left-click and drag this selection of scans to the
appropriate floor.

Figure #14 - Select & Drag the New Scans from the New Floor to the Initial Floor

10

*Note: Best practice is to add new data underneath the existing (keeping it in order oldest to newest).
12) Rotate and place the new data to the side of the original data.

Figure #15 - New Scans Set Next to the Old Scans & Floor Plan

13) Once the new data has been moved to the appropriate floor, it is unlikely the
scans will be in the correct position. From here, use “3” in “M Mode” to
automatically place the scans in the correct position & location. Use this feature
for each individual pano (scan). Keep an eye on the scans as they get placed
automatically. Make adjustments as necessary right away to ensure it’s in the
correct location. In certain situations, this method may not work and manual
alignment will be required.
a) Once all new data has been placed, double check that the alignment of
the new data actually makes sense.
11

Figure #16 - Using “M Mode” #3 to Place Scans in the Correct Locations

14) Now that the data is confirmed to be in the correct location, the older scans
that are overlapping or occupying the same spaces as the new data, disable the
visuals for the old data.
a) If both the new scan and the old scan are enabled, deactivate the old
scan.
b) If both the new scan and the old scan are disabled, then leave them as is.
c) If the new scan is disabled and the old scan is enabled, leave as is.
d) If the new scan is enabled and the old scan is disabled, leave as is.

12

15) Middle click each pano to disable or if it’s a full pano replacement, select all the
panos in the Project Explorer. right-click the selection, scroll over to “Selected
Scans” and select “Disable in Portal”.

Figure #17 - Disable Old Scans for Spaces in Which a New Scan has been Placed

13

Figure #18 - Old Scans are Disabled on the Portal

14

16) Right-click off to the side of the floor plan and select auto-place all room labels.
This will best fit the room labels due to the new enabled scan locations.

Figure #19 - Auto-place All Room Labels to Accommodate the New Scan Placements

17) This process will be repeated for each floor new data was provided for.

15

*Warning: Make sure there are no remaining scans/data in a floor of the “new
building” before deleting. The floors must be completely empty before deleting. A file
cannot be exported and uploaded to an iGUIDE Portal with empty floor or empty
buildings.
18) Once the new data has been moved to the correct corresponding floor(s)
proceed to delete the redundant empty building and associated empty floor(s).

Figure #16 - Delete Empty Redundant Building

16

19) Review the alignment of the new scans to ensure nothing is misaligned.
20) Click the verify button to ensure there are no errors. Mitigate any pending
warnings if applicable.
21) Save, Export then close the project.
22) On the Task Details Page scroll down to the comments section to describe what
was done for the update. For any update task it is best practice to leave a
comment to confirm what changes were made. This serves as a changelog
(revision history) and gives Planitar better traceability of events.

Figure #8 - Description of Work Performed for the Workorder/Task

23) On the Task Details Page, scroll back up to the “Draft Data (Staging Area)” and
select the white “Toggle Upload Interface” button.
a) Drag and drop or click to select the new exported “draft.tar” file into the
gray dashed box.

17

Figure #20 - Toggle Upload Interface and Drag & Drop the draft.tar

24) After dropping or selecting the “draft.tar", ensure that the checkbox “Publish to
iGUIDE upon upload” is checked and the “Send iGUIDE Report” checkbox is
unchecked.
a) We want to publish the Update.
b) We do not want to resend the iGUIDE Report.
25) Finally, select the large blue “Upload” button and wait for the update to publish
to the Portal.
*Note: While the iGUIDE update is processing (uploading back to the Portal), start on
the next task in the queue.

18

Figure #21 - Publish iGUIDE Upon Upload, Do Not Send the Report and Select Upload

19

26) Once the status bar reaches 100%, a green prompt reminding us to send the
iGUIDE Report will signify that the upload was successful and the work order is
complete.
a) Do not send the iGUIDE Report.
b) Close the task and it’ll appear under “Done” in the “My Work Orders”
section of the Master Queue.

Figure #22 - Update Successfully Completed

20

Draft Update Procedure (Floor Plan Update)
The procedure at a glance is to download the published iGUIDE, download the new
stitch data (if provided), merge the new stitch data into the published file, replace the
panos (insert new, deactivate old), make structural changes, add missing rooms or
missing floors, then reupload the project back to the Portal.
1) While in the QA Queue, select the blue “claim next work order” button.

Figure #23 - Claim Next Work Order

2) After claiming the work order, the Task Details Page will open with the Quality
Technician as the claimer listed under the QA section. No name will be listed
under the Drafter section as there is no Draft to QA workflow for updates. Only
Quality Technicians handle these kinds of tasks.
a) The Description field will indicate what is involved with the update.
b) The Description field for this example indicates that the operator would
like us to process this as a Floor Plan Update.
*Note: Some descriptions are very thorough, others are not so some investigation
may be required.

21

Figure #24 - Reviewing the Description of the Floor Plan Update

3) Review any images provided in the “Supporting Documents” section to help
better understand the request. Some requests may or may not have Supporting
Documents.

Figure #25 - Example “Supporting Documents”

22

4) Scroll down to the “Stitch Data” section. Click on the blue “Download Original
Stitch Data” button. This will download the operator's new additional panos
(scans) to be added to the initial iGUIDE.

Figure #26 - Stitch Data: Download Original Stitch Data

5) Scroll down further down to the “Published Draft Data” section and click the
“Download published Draft data” button. This will download the initial published
iGUIDE data.
*Note: For an update involving an iGUIDE that is in pre-published state, this section
will be displayed as “Pre-published Draft Data” and the blue button will read,
“Download pre-published Draft data”.

Figure #27 - Published Draft Data: Download Published Draft Data

23

a) The Initial iGUIDE will appear with the “draft.tar” file extension within the
downloads folder. The new data to be added will appear with the
“orig-stitch-data.tar” file extension.

Figure #28 - Downloads Folder: draft.tar (old) & orig-stitch-data.tar (new)

6) Once both sets of data have been downloaded, open the Initial iGUIDE (draft.tar)
using Draft.

Figure #29 - Select the draft.tar to Open in Draft First

24

7) Once the Initial draft.tar has been opened within Draft, right-click the property
address within the Project Explorer, click “Merge with Existing Project” and select
the file with the “orig-stitch-data.tar” file extension.

Figure #30 - Merge with Existing Project

25

Figure #31 - Select the orig-stitch-data.tar to Merge

8) AI Processing will begin and last anywhere from less than a minute to upwards
of an hour depending on the size of the update.
*This is on R&D’s Roadmap to have AI processing happen on the Portal as opposed to Draft.

Figure #32 - Waiting to Finish AI Background Processing

9) The new data will appear as a new “Main Building” with subsequent floors.
Right-click on the new data’s “Main Floor” and select “Add Asterisk to Scan
Names”. This adds a visual indicator for the Drafting Team and Support Team to
know that this iGUIDE has been updated. This also helps the QA working with
the update to differentiate between the old data and new data.
26

Figure #33 - Add Asterisk to Scan Names

10) Select all of the new scans and drag & drop them to the correct corresponding
floo. You may have to investigate what floor they belong to, however oftentimes
operators will name the floor correctly for where the new data is to be placed.
The example image below shows that the new data is under the “Basement”
floor, so this new data will be dragged into the “Basement” floor of the drafted
data.
*Note: Best practice is to add new data underneath the existing (keeping it in order oldest to newest).

27

Figure #34 - Drag & Drop to Correct Floor

*Warning: Make sure there are no remaining scans/data in a floor of the “new
building” before deleting. The floors must be completely empty before deleting. A file
cannot be exported and uploaded to an iGUIDE Portal with empty floor or empty
buildings.
11) Once the newly submitted data has been moved to the correct corresponding
floors proceed to delete the redundant empty building and associated empty
floors.

28

Figure #35 - Delete Empty Redundant Building

12) Select all the scans with the asterisk now that they’re in the appropriate floor.
Rotate the data to match the orientation of the existing drafted floor and set the
new scans off to the side of the floor plan for clarity.

29

Figure #36 - Select the New Data and Orient it

13) You can attempt to use #3 while in “M” Mode to auto-place the new data, the
same way as in pano updates. This will work as long as the new data is similar to
the old. However, it may not work well when adding new data or captures with
significant structural changes. In the event that this function does not work or
only partially works, proceed to manually align all of the new data to the old set
of data.

30

Figure #37 - Align the New Data Set to the Old Data Set

14) When there is new data for a room or space previously captured, deactivate the
older scans. You can do this all at once by selecting all the appropriate data
without an asterisk or go scan by scan deactivating them one at a time.
a) If both the new scan and the old scan are enabled, deactivate the old
scan.
b) If both the new scan and the old scan are disabled, then leave them as is.
c) If the new scan is disabled and the old scan is enabled, leave as is.
d) If the new scan is enabled and the old scan is disabled, leave as is.
*Note: It is important that only the areas with new scans require the older scans to be
deactivated. Do not deactivate the old unless there’s something new to replace it.
31

*Note: NEVER delete older data unless the operator specifically requests us to do so.
We always keep the older data and deactivate if applicable (overlapping enabled
scans).

Figure #38 - Disable Older Applicable Scans

15) Once the new data has been aligned proceed to draft/redraft the applicable
changes. This can range from simple structural changes (finishing a basement
similar to the image below) or adding in a missing space.

32

Figure #39 - Draft/Redraft Based on the New Data

16) Once the new data has been drafted/redrafted perform a double check that
everything newly completed is correct. Verify that there are no errors when
exporting the property, fixing any if applicable before finally saving, exporting
and closing the project.
33

17) Returning to the Task Details Page of the current Workorder, scroll down to the
comments section to describe what was done for the update.

Figure #40 - Description of Work Performed for the Workorder/Task

18) Scroll up to the “Draft Data (Staging Area)” and select “Toggle Upload Interface”.
a) Drag and drop or click to select the new exported draft.tar file .

Figure #41 - Toggle Upload Interface and Drag & Drop the draft.tar

34

19) After dropping or selecting the draft.tar, ensure that the checkbox “Publish to
iGUIDE upon upload” is checked and the “Send iGUIDE Report” is unchecked.
a) We want to publish the Update.
b) We do not want to resend the iGUIDE Report.
20) Finally, select the large blue “Upload” button and wait for the update to publish
to the Portal.

35

Figure #42 - Publish iGUIDE Upon Upload, Do Not Send the Report and Select Upload

36

*Note: While the iGUIDE update is processing (uploading back to the Portal), start on
the next task in the queue.
21) Once the status bar reaches 100%, a green prompt reminding us to send the
iGUIDE Report will signify that the upload was successful and the work order is
complete.
a) Do not send the iGUIDE Report.
b) Close the task and it’ll appear under “Done” in the “My Work Orders”
section of the Master Queue.

Figure #43 - Update Successfully Completed

37

Draft Update (Other?)
The two most typical Draft Updates are Floor Plan Updates to add in missing
spaces/new spaces or Pano Updates to replace visuals. Both of these update types
contain new Stitch Data provided by the operator, however some Draft Updates may
not actually contain new Stitch Data.
Examples of Draft Updates without new data and without changing the task to a
courtesy type may involve us duplicating floor plans, splitting up floor plans or merging
floor plans together. Relate this to a backsplit or side split property, if the operator
originally submitted four separate floor plans and it was published as such, the
operator could choose to create a Draft Update to merge floors together. The Quality
Technician would then proceed with merging floors together as specified by the
operator without adding any new data.

38

