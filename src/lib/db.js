// TODO phase this file out in favor of mongoose
import { MongoClient } from "mongodb";

const uri = process.env.MONGODB_URI;

const options = {};

let client;
let cornhub_db;

/**
 * Connects to the mongodb database with the `mongodb` driver
 * @returns the db connection to the "cornhub" database
 */
async function connectToDatabase() {
  // The correct way of dealing with an ambiguous connection is to just call MongoClient.connect() again
  // If you're already connected nothing will happen (it is a NOOP/no-operation), and if there is not already a connection you'll be connected (as expected).
  client = await MongoClient.connect(uri, options);
  cornhub_db = client.db(); // if no argument is provided, by default get the db in connection string ("cornhub")
  return cornhub_db;
}

/**
 * Utility function to query all groups a user is associated to.
 * @param {*} user_id the uuid of the user
 */
async function getGroupsAssociatedWithUser(user_id) {

}

export default { getGroupsAssociatedWithUser, connectToDatabase };
