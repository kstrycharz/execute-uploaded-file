
<?php
// Check if the form has been submitted
if(isset($_POST['submit'])){


    // Check if a file has been selected for upload
    if(isset($_FILES['fileToUpload'])){


        // Define the target folder
        $target_folder = "documents/";

        // Get the file name
        $file_name = basename($_FILES['fileToUpload']['name']);


        // Define the target path
        $target_path = $target_folder . $file_name;


        // Attempt to upload the file
        
        
        
        if(move_uploaded_file($_FILES['fileToUpload']['tmp_name'], $target_path)){


            echo "The file ". $file_name . " has been uploaded.";
        } else {
            echo "There was an error uploading the file, please try again.";
        }
    }
}
?>