import { Route, Routes } from "react-router-dom";
import User from "./pages/User";

export function AppRoutes(){
    return (
        <Routes>
            <Route path="/user" element={<User />}/>
        </Routes>
    );
}