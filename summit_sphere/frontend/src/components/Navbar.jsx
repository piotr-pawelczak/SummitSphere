import { AppBar, styled, Toolbar, Typography } from "@mui/material";

const StyledToolbar = styled(Toolbar)({
  display: "flex",
  justifyContent: "space-between",
});

function Navbar() {
  return (
    <AppBar position="sticky">
      <StyledToolbar>
        <Typography variant="h6">SUMMIT SPHERE</Typography>
      </StyledToolbar>
    </AppBar>
  );
}
export default Navbar;
