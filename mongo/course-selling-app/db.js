const mongoose = require('mongoose');
const logger = require('./utils/logger');

require('dotenv').config();


async function connectDB() {
    try{
        await mongoose.connect(process.env.MONGO_URI);
        logger.info(`Successfully Connected to DB`);
    }
    catch(error){
        logger.error(`Error connecting to DB. ${error}`)
        process.exit(1);
    }
}

const Schema = mongoose.Schema;

const UserModel = new Schema({
    "first_name": {type: String, required: true},
    "last_name":{type: String, required: true},
    "email": {type: String, required: true},
    "password": {type: String, required: true}
})

const CourseModel = new Schema({
    title: 'description',
})


const users = mongoose.model('users', UserModel)

module.exports = {users, connectDB};

