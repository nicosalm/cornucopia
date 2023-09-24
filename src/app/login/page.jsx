"use client";

import { useState } from "react";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();

    // TODO login stuff
    // console.log(`logging in w/ email ${email}, password ${password}`);
    
    
  };

  return (
    <div className="flex justify-center items-center h-screen">
      <form
        onSubmit={handleSubmit}
        className={`site-primary-bg site-secondary p-8 rounded-md shadow-mid border`}
      >
        <h1 className="site-text text-2xl font-bold mb-4">Login</h1>
        <label className="block mb-4">
          Email:
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className="block w-full site-text-bg rounded-md mt-2 p-3 text-s text-black"
          />
        </label>

        <label className="block mb-4">
          Password:
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="block w-full site-text-bg rounded-md mt-2 p-3 text-s text-black"
          />
        </label>

        <button
          type="submit"
          className="text-white mt-3 py-2 px-4 rounded-md bg-green-700 hover:bg-green-600"
        >
          Login
        </button>
      </form>
    </div>
  );
}
