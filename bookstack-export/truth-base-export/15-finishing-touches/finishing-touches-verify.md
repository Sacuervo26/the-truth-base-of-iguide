1 
 
Finishing Touches: Part 2 - 
Verify 
 
Verify  
It’s important to use the Verify button for consolidating errors and warnings. All errors must be 
solved before uploading the file to the Portal (some exceptions for drafters). Warnings can be 
ignored before uploading the file to the Portal as long as they’re understood and won’t affect 
the end result.   
 
Once the draft has been finished the Verify button must be used.   
 
 
Figure 1 - Verify Button 
 
 
 


 
2 
Resolving Warnings and Errors  
Errors 
 
These are conditions that cannot be ignored and the file cannot be published on the Portal 
until the error is resolved.  
 
● Error Message: “Floorplan is outside the printable area of the SVG standard. Press G, 
zoom out, and bring it inside the white square area.” 
Solution: Press G, zoom out, and bring it inside the white square area. 
 
● Error Message: “Wall item can't be attached to thin lines.” 
Solution: Windows and doors cannot be attached to thin lines. Remove the window or 
door. 
 
● Error Message: “One of the lines has size bigger than the 500m limit. How did it 
happen? Remove this line or save your work and reload the property ASAP or, Line 
bigger than the 500m limit.” 
Solution: Remove this line or save your work and reload the property. 
 
● Error Message: “Initial pano was not set.” 
Solution: Automatically makes you choose an initial pano if one is not set. 
 
● Error Message: “Property has no main building.” 
Solution: Choose one of the buildings, right click it on the project explorer and choose 
Set as the main building. 
 
● Error Message: “Main Building is not enabled on the Portal.” 
Solution: Make sure the main building is active by middle clicking it on the project 
explorer removing the red X through it. 
 
● Error Message: “Building is empty.” 
Solution: Assign the proper floors to the proper buildings and delete any empty 
buildings. 
 
● Error Message: “No compass data. Ensure all floors have the same orientation.” 
Solution: Some floors have compass data while others don’t, set the ones without 
compass data to independent, by clicking on the floor and checking the box 
“independent orientation and compass. 


 
3 
 
● Error Message: “Wall item is not attached to wall.” 
Solution: There is a window or door not attached to a wall, find it and delete it. 
 
● Error Message: “Gate is not paired.” 
Solution: Pair all gates and/or delete any that lead to a floor with no laser data. 
 
● Error Message: “Room has no name but label is still visible.” 
Solution: There is no text within the label, make sure there is some text within the label 
or delete the label. 
 
● Error Message: “Room name is mandatory for this room type.” 
Solution: A room was given a type, but not a name. This room must be given a name. 
 
● Error Message: “Cross-arrow rotation is unconventional (Y axis should be pointing up).” 
Solution: The red cross arrows are rotated incorrectly, click the  “Auto rotate ALL cross 
arrows” or manually adjust. 
 
● Error Message: “Label Text not set.” 
Solution: There is a manual label called “Text” which is the default text to show up, 
make sure it is changed to the correct name. 
 
● Error Message: “Coinciding lines leaving the same vertex (same angle).” 
Solution: Move the vertex away and delete the extra line segment. 
 
● Error Message: “Panoramas are closer than 50 cm. Adjust room position or disable it.” 
Solution: Disable one pano only (Drafters will not disable, only QA - ignore this error). 
 
● Error Message: “Overlap between rooms. Trace a divider line between the internal and 
external rooms.” 
Solution: There is a room inside another room, place a divider between them. 
 
● Error Message: “Is neither a floor plan (has rooms) or common area (has panos only).” 
Solution: There is a floor with no panos within it. Either add the corresponding panos 
or delete the floor. 
 
● Error Message: “Print label '" + currRoom->getName() + "' is outside the room area. 
Select the room first if it is covered by another room.” 
Solution: Delete the room label and room type then relabel the space.  
 


 
4 
● Error Message: “Viewer label '" + currRoom->getName() + "' is outside the room area. 
Select the room first if it is covered by another room.” 
Solution: Delete the room label and room type then relabel the space.  
 
● Error Message: "Ceiling height is smaller than camera height." 
Solution: Set the ceiling height so that it is above the camera height. 
  
● Error Message: "Is neither a floorplan (has rooms) or common area (has panos only)." 
Solution: Nothing has been drafted so the file cannot be published to the Portal. The 
property will be refused if there is nothing to draft.  
 
 


 
5 
Warnings 
 
These are conditions that can be ignored when applicable, but should be resolved whenever 
possible.  
 
● Warning Message: “Duplicated building name.” 
Solution: Change the name of one of the buildings. 
 
● Warning Message: “Big floor with horizontal aspect ratio. Should we rotate it 90 deg?” 
Solution: Rotate the floor(s) to be portrait rather than landscape. 
 
● Warning Message: “No compass data. “ 
Solution: No floors have compass data. No solution for this.  
 
● Warning Message: “Compass angle differs significantly, should it be compass 
independant?” 
Solution: Rotate floors so they all have the same orientation. This can be sensitive so 
only rotate floors if there is a difference greater than 90°. 
 
● Warning Message: “Wall item is not fully contained in its parent wall.” 
Solution: A door/window is overlapping 2 or more sections of wall. Make sure the 
object is placed properly on the wall. If placed properly, ignore the warning. 
 
● Warning Message: “Invisible divider is not splitting any room (same room on both 
sides).” 
Solution: Delete the unnecessary invisible divider. 
 
● Warning Message: “Possible drawing artifact.” 
Solution: A drawn line has gone past the expected end by a very small amount. Delete 
the extra line segment. 
 
● Warning Message: “Couldn’t find a path between some of the rooms.” 
Solution: Make sure every room has a door and can be accessed from other rooms. A 
garage with no door to the house may be an exception to this.  
 
● Warning Message: “Arrows dimension differs from room bounding rectangle.” 
Solution: Move crosshair arrows to maximize the bounding box of the room. 
 


 
6 
● Warning Message: “Opposite arrows may not be aligned.” 
Solution: The left and right or up and down dimension arrows are no longer lined up 
(sometimes this can’t be avoided if the bounding box for the room is oddly shaped). 
 
● Warning Message: “Dimension arrow is outside (or partially) room area.” 
Solution: The room dimension arrow(s) are outside the bounding box of the room. 
They should be moved within the bounding box (unless they are manually moved out to 
encompass Restricted Height areas. 
 
● Warning Message: “Initial pano is not enabled on the portal.” 
Solution: Ignore this warning. The initial pano can be changed later on the portal by 
someone who has access to edit the iGUIDE.  
 
● Warning Message: “Room label rotation is unconventional.” 
Solution: Room label is partially upside down when compared to the rest of the rooms, 
rotate the label to match the rest (0° or 90°). 
 
● Warning Message: “Room label is rotated in a room that seems not to be rotated (may 
look bad).” 
Solution: Room label is rotated on an angle other than 0° or 90°, rotate it to match one 
of these angles. 
 
● Warning Message: “Label is rotated (are you sure?).” 
Solution: Manual label is rotated when it should be only 0°. 
 
● Warning Message: “Wall intersection.” 
Solution: Two or more line segments are partially intersecting and no node has been 
created. Make sure the lines are drawn correctly (although often this warning can be 
ignored). 
 
● Warning Message: “Label intersection with Panorama.” 
Solution: A room or manual label is intersecting with a point, move the label so they 
are no longer intersecting. If space is an issue, reduce the size of the text.  
 
● Warning Message: “Overlap between labels.” 
Solution: 2 or more labels (manual or room) are overlapping, move one or more of 
them so they are no longer overlapping. 
 
 


 
7 
● Warning Message: “Interior area is zero.” 
Solution: The entire floor has its square footage excluded from the total square 
footage of the home (This can happen for stand alone buildings). Include the area if 
only if applicable. 
 
● Warning Message: “Are you sure this floor is below grade?” 
Solution: A floor with “floor”, ”level”, ”loft” or ”attic” in the floor name has been checked 
as below grade. This setting must not be touched.  
 
● Warning Message: “Are you sure this floor is above grade?” 
Solution: Basement and or a floor with “Lower” in the name has not been checked as 
below. This setting must not be touched.  
 
● Warning Message: Gate is not visible by any Scan. 
Solution: Delete the gate(s). 
 
● Warning Message: Make sure this stair is not outside (e.g. cosmetic stairs in backsplit 
floors). 
Solution: Mark the stairs as exterior or ensure they are not bound in exterior spaces. 
 
● Warning Message: “Floor has no window" 
Solution: Double check that there are no missing windows. Some floors do not have 
any windows.