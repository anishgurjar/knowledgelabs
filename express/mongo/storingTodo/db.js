const mongoose = require('mongoose');
const Schema = mongoose.Schema;
const ObjectID = mongoose.SchemaTypes.ObjectId;
require('dotenv').config();

async function conenctDB(){
    try{
        console.log(process.env.MONGO_URI);
        await mongoose.connect(process.env.MONGO_URI);
        console.log("DB connection successful");
    }
    catch(error){
        console.log(`Error: ${error}`);
    }
}

const users = new Schema({
    "username": {type: String, required: true, unique: true},
    "password": {type: String, required: true}
})

const todos = new Schema({
    "title": {type: String, required: true},
    "done?": {type: Boolean, required: true},
    "userID": ObjectID
})

//create models
const UserModel = mongoose.model('users', users)
const TodoModel = mongoose.model('todos', todos)

module.exports = {UserModel, TodoModel, conenctDB}
