import React, { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

export default function ProtectedRoutes({children})
{
    const navigate = useNavigate()

    const user = localStorage.getItem('current_user')
    const isAuthenticated = user ? localStorage.getItem(`${user}_access_token`):null

    useEffect(()=>{
        if (!isAuthenticated) navigate('/login')

    },[])

}