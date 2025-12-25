import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import '../index.css'

export default function LoginUser(){

    const [formData,setFormData]  = useState({"username": "","password" : ""})
    const [msg, setMsg] = useState("");
    const navigate = useNavigate()

    const handleChange = (e) => {

        setFormData({
            ...formData,
            [e.target.name] : e.target.value

        })
    }

    const handleSubmit = async(e) => 
    {
        e.preventDefault()

        try{

            const response = await axios.post("http://127.0.0.1:8000/api/login",
                formData
            )

            const { message,access_token, refresh_token,user,error}= response.data

            if (user) {
            // Store tokens with username prefix
            localStorage.setItem('current_user',user.username)
            localStorage.setItem('current_user_id',user.id)
            localStorage.setItem(`${user.username}_access_token`, access_token);
            
            localStorage.setItem(`${user.username}_refresh_token`, refresh_token);
            }
            
            if(response.status == 200){
                navigate("/bookride")
            }
             
             setMsg(message ? message: error)
            //  console.log("login successful")
        }
        catch(err)
        {
            setMsg(err.response?.data?.error || "Login failed");
        }
    }


    return(  <>
      <h2>Login</h2>

      <form onSubmit={handleSubmit}>

        <input
          type="text"
          name="username"
          placeholder="Username"
          value={formData.username}
          onChange={handleChange}
          required
        />

        <br /><br />

        <input
          type="password"
          name="password"
          placeholder="Password"
          value={formData.password}
          onChange={handleChange}
          required
        />

        <br /><br />

        <button type="submit">Login</button>
      </form>

      {msg && <p>{msg}</p>}
    </>
    )
}