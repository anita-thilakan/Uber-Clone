import { BrowserRouter, Routes, Route } from "react-router-dom";
import RegisterRiders  from './pages/Riderregister_api.jsx'
import LoginUser  from "./pages/LoginUser.jsx";
import BookRide from "./pages/BookRide.jsx";
import ProtectedRoutes from "./pages/ProtectedRoutes.jsx";
function App() {
  
  return (
    <>
    
    <BrowserRouter>
      <Routes>
        <Route path="" element={<RegisterRiders />} />
        <Route path="/login" element={<LoginUser />} />
        <Route path="/bookride" element ={

          <ProtectedRoutes>
          <BookRide/>
          </ProtectedRoutes>
          
          } />
      </Routes>
    </BrowserRouter>
   </>   
  )
}

export default App
