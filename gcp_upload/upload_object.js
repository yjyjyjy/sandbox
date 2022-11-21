/**
 * TODO(developer): Uncomment the following lines before running the sample.
 */
// The ID of your GCS bucket
const bucketName = 'hireacross-test';

// The path to your file to upload
// const filePath = 'helmet.jpeg';
const filePath = '';
const localFileName = 'sample-5s.mp4';

// The new ID for your GCS file
// const destFileName = 'helmet.jpeg';
const destFileName = localFileName

// Imports the Google Cloud client library
const { Storage } = require('@google-cloud/storage');

// Creates a client
const storage = new Storage({ keyFilename: 'hireacross-f827f800318b.json' });

async function uploadFile() {

    // let generationMatchPrecondition = 0

    const options = {
        destination: destFileName,
        // Optional:
        // Set a generation-match precondition to avoid potential race conditions
        // and data corruptions. The request to upload is aborted if the object's
        // generation number does not match your precondition. For a destination
        // object that does not yet exist, set the ifGenerationMatch precondition to 0
        // If the destination object already exists in your bucket, set instead a
        // generation-match precondition using its generation number.

        // preconditionOpts: { ifGenerationMatch: generationMatchPrecondition },
    };

    await storage.bucket(bucketName).upload(filePath + localFileName, options);
    console.log(`${filePath} uploaded to ${bucketName}`);
}

uploadFile().catch(console.error);