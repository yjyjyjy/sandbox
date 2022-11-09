
// const Cloud = require('@google-cloud/storage')

import Cloud from '@google-cloud/storage'
// const path = require('path')
import path from 'path'
import { fileURLToPath } from 'url';
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const serviceKey = path.join(__dirname, './hireacross-f827f800318b.json')

const { Storage } = Cloud
const storage = new Storage({
    keyFilename: serviceKey,
    projectId: 'hireacross',
})
export default storage

// module.exports = storage