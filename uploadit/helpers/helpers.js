// const util = require('util')
import util from 'util'
// const gc = require('./config/')
// import gc from '../config/index.js'
// import { storage } from '../config/index.js'
import storage from '../config/index.js'
const bucket = storage.bucket('image-upload-tutorial') // should be your bucket name

/**
 *
 * @param { File } object file object that will be uploaded
 * @description - This function does the following
 * - It uploads a file to the image bucket on Google Cloud
 * - It accepts an object as an argument with the
 *   "originalname" and "buffer" as keys
 */

export const uploadImage = (file) => new Promise((resolve, reject) => {
    const { originalname, buffer } = file
    console.log(originalname)

    const blob = bucket.file(originalname.replace(/ /g, "_"))
    const blobStream = blob.createWriteStream({
        resumable: false
    })

    blobStream.on('finish', () => {
        const publicUrl = format(
            `https://storage.googleapis.com/${bucket.name}/${blob.name}`
        )
        resolve(publicUrl)
    })
        .on('error', () => {
            reject(`Unable to upload image, something went wrong`)
        })
        .end(buffer)
})