# Remote Image Channel Decompilation Assembler 9000

As the name suggests, this program consists of a server running Flask which receives images, splits them into the RGB channel seperately and returns them to the client. 
Then, the client merges the B&W images representing the different channels into a single colour image.

## Running
Initially, run the server using the `/server/server.py` file using `python server.py`.\
*NOTE: Edit the path to the RGB Channel images which suit your system.*

Add the `file.jpg` to the client folder, the image to be sent to the server. 

Run `python client.py` to send the image. This is the second and last step. The merged image is saved as `/client/merged.jpg`. 
