// const express = require('express')
import express from 'express'
import bodyParser from 'body-parser'
// const bodyParser = require('body-parser')
import multer from 'multer'
// const multer = require('multer')
import { uploadImage } from './helpers/helpers.js'
// const uploadImage = require('./helpers/helpers')

const app = express()

const multerMid = multer({
    storage: multer.memoryStorage(),
    limits: {
        // no larger than 5mb.
        fileSize: 5 * 1024 * 1024,
    },
})

app.disable('x-powered-by')
app.use(multerMid.single('file'))
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: false }))

app.post('/uploads', async (req, res, next) => {
    try {
        const myFile = req.body.file
        console.log(myFile)
        const imageUrl = await uploadImage(myFile)
        res
            .status(200)
            .json({
                message: "Upload was successful",
                data: imageUrl
            })
    } catch (error) {
        next(error)
    }
})

app.use((err, req, res, next) => {
    res.status(500).json({
        error: err,
        message: 'Internal server error!',
    })
    next()
})

app.listen(9001, () => {
    console.log('app now listening for requests!!!')
})