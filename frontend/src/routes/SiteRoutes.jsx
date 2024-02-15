import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Filesystem from "../components/Filesystem.jsx";


const SiteRoutes = () => {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Filesystem />} />
            </Routes>
        </Router>
    );
};

export default SiteRoutes;