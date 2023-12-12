import * as React from "react";
import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import CssBaseline from "@mui/material/CssBaseline";
import Divider from "@mui/material/Divider";
import Drawer from "@mui/material/Drawer";
import IconButton from "@mui/material/IconButton";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemButton from "@mui/material/ListItemButton";
import ListItemText from "@mui/material/ListItemText";
import MenuIcon from "@mui/icons-material/Menu";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import Button from "@mui/material/Button";
import styled from "@mui/material/styles/styled";

const drawerWidth = 240;
const navItems = ["Home", "About", "Contact"];
const logoText = "SUMMIT SPHERE";

const StyledButton = styled(Button)({
  color: "#fff",
  ":hover": {
    color: "#1abc9c",
  },
});

const StyledListItemButton = styled(ListItemButton)({
  color: "#fff",
  ":hover": {
    color: "#1abc9c",
  },
});

function DrawerNavbar(props) {
  const { window } = props;
  const [mobileOpen, setMobileOpen] = React.useState(false);

  const handleDrawerToggle = () => {
    setMobileOpen((prevState) => !prevState);
  };

  const drawer = (
    <Box onClick={handleDrawerToggle} sx={{ textAlign: "center"}}>
      <Typography variant="h6" sx={{ my: 2 }} color="secondary">
        {logoText}
      </Typography>
      <Divider/>
      <List>
        {navItems.map((item) => (
          <ListItem key={item} disablePadding>
            <StyledListItemButton sx={{ textAlign: "center" }}>
              <ListItemText primary={item}/>
            </StyledListItemButton>
          </ListItem>
        ))}
      </List>
    </Box>
  );

  const container =
    window !== undefined ? () => window().document.body : undefined;

  return (
    <Box sx={{ display: "flex"}} position={"fixed"} zIndex={1000}>
      <CssBaseline />
      <AppBar component="nav" color="background" elevation={0}>
        <Toolbar>
          <IconButton
            color="secondary"
            aria-label="open drawer"
            edge="start"
            onClick={handleDrawerToggle}
            sx={{ mr: 2, display: { sm: "none" } }}
          >
            <MenuIcon />
          </IconButton>
          <Typography
            variant="h6"
            component="div"
            sx={{ flexGrow: 1 }}
            color="secondary"
            fontFamily={"Montserrat"}
          >
            {logoText}
          </Typography>
          <Box sx={{ display: { xs: "none", sm: "block" } }}>
            {navItems.map((item) => (
              <StyledButton key={item}>
                {item}
              </StyledButton>
            ))}
          </Box>
        </Toolbar>
      </AppBar>
      <nav>
        <Drawer
          container={container}
          variant="temporary"
          open={mobileOpen}
          onClose={handleDrawerToggle}
          ModalProps={{
            keepMounted: true, // Better open performance on mobile.
          }}
          sx={{
            display: { xs: "block", sm: "none" },
            "& .MuiDrawer-paper": {
              boxSizing: "border-box",
              width: drawerWidth,
              backgroundColor: "background.main",
              color: "text.main",
            },
          }}
        >
          {drawer}
        </Drawer>
      </nav>
    </Box>
  );
}

export default DrawerNavbar;
