
import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

import '../index.css'

export default function  RegisterRiders() {

    const navigate = useNavigate();

    const [formData, setFormData] = useState({
        username : "",
        email : "",
        phone : "",
        password : "",
        payment_method : "",
        default_pick_up : ""

    });

    const [msg, setMsg] = useState("");

    const handleChange = (e) => {

        setFormData({

            ...formData,
            [e.target.name]: e.target.value
        });


        

    };

    const handleSubmit = async(e) => {
        e.preventDefault() // stops the page from reload
        // console.log(formData)
        try { 
            const res = await axios.post("http://127.0.0.1:8000/api/register/rider",formData,
                {
                    headers: {
                    "Content-Type": "application/json"
                    }
                }

            
            );
            // console.log(res.data)
            if(res.status == 201)
            {
               // Redirect to login or home
            navigate("/login");  
            return;
            }
            
            
        }
        catch(err)
        {
             setMsg(err.response?.data?.error || "Registration failed");



        }

    }

    return (
    <>
      <h2>Register</h2>

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="username"
          placeholder="Name"
          value={formData.username}
          onChange={handleChange}
        /><br /><br />

        <input
          type="email"
          name="email"
          placeholder="Email"
          value={formData.email}
          onChange={handleChange}
        /><br /><br />

        <input
          type="password"
          name="password"
          placeholder="Password"
          value={formData.password}
          onChange={handleChange}
        /><br /><br />

        <input
          type="text"
          name="phone"
          placeholder="Mobile Number"
          value={formData.phone}
          onChange={handleChange}
        /><br /><br />

       <select name="payment_method" value={formData.payment_method} onChange={handleChange}>
          <option value="">-- Select --</option>
          <option value="upi">UPI</option>
          <option value="cash">CASH</option>
        </select>
        <br /><br />

        <input
          type="text"
          name="default_pick_up"
          placeholder="default_pick_up"
          value={formData.default_pick_up}
          onChange={handleChange}
        /><br /><br />

        <button type="submit">Register</button>
        <br/> <br/>
        <button onClick={() => navigate("/login")} >
        Login
      </button>
      </form>

      {msg && <p>{msg}</p>}
    </>
  );


}