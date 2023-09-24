import Cookies from "js-cookie";
import mongoose from "mongoose";

const userSchema = mongoose.Schema({
  user_name: { type: String, required: true, unique: true },
  password: { type: String, required: true },
});

/**
 * Takes a username and password and attempts to verify the hashed password matches with the one in the server.
 * Returns a JWT for the client to use for their session.
 * @param {string} user_name the user's username
 * @param {string} password (unhashed) the user's password
 * @returns a JWT (json web token) for the (approved) client
 */
export async function loginUser(user_name, password) {
  mongoose.connect(process.env.DB_URI);
  
  const User = mongoose.model("User", userSchema);

  try {
    const user = await User.findOne({ user_name, password });
    console.log(`found the user: ${user}`);
  } catch (err) {
    console.log('couldnt find that user');
  }
}
