import React from 'react';
import {
  ChakraProvider,
  Box,
  Flex,
  Spacer,
  Avatar,
  Menu,
  MenuButton,
  MenuList,
  MenuItem,
  Text,
  CSSReset,
} from '@chakra-ui/react';
import {useNavigate} from "react-router-dom"
import { EditIcon, CloseIcon } from '@chakra-ui/icons';

const NavBar = () => {

  const navigate = useNavigate();

  const handleLogout = async () => {
    try {
      const response = await fetch("http://localhost:5000/logout", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
      });

      if (response.ok) {
        sessionStorage.clear();
        navigate("/Authentification");
      } else {
        console.error("Error connection", response.statusText);
      }
    } catch (error) {
      console.error("Error:", error.message);
    }
  };
  return (
    <ChakraProvider>
      <CSSReset />
      <Flex p={2} colorScheme={'blue'} bg={'blue.400'} >
        {/* SmartParking text */}
        <Text color="white" fontWeight="bold" fontSize="3xl">
          SmartParking.
        </Text>

        <Spacer />

        {/* Dropdown menu button */}
        <Box>
          <Menu>
            <MenuButton as={Avatar} name="Dan Abrahmov" src="https://bit.ly/dan-abramov" variant="outline" />
            <MenuList>
              <MenuItem icon={<EditIcon />}>Edit Account</MenuItem>
              <MenuItem icon={<CloseIcon />} onClick={handleLogout}>Logout</MenuItem>
            </MenuList>
          </Menu>
        </Box>
      </Flex>
    </ChakraProvider>
  );
};

export default NavBar;
