import DrawerNavbar from "./components/DrawerNavbar";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Container } from "@mui/material";
import SummitList from "./pages/SummitList";

function App() {
  return (
    <BrowserRouter>
      <DrawerNavbar />
      <Container maxWidth="lg" sx={{ paddingTop: 10}}>
        <Routes>
          <Route path="/" element={<SummitList />} />
          <Route path="/about" element={<h1>About</h1>} />
          <Route path="/contact" element={<h1>Contact</h1>} />
        </Routes>
      </Container>
    </BrowserRouter>
  );
}

export default App;
