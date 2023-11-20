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
import { EditIcon, CloseIcon } from '@chakra-ui/icons';

const NavBar = () => {
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
              <MenuItem icon={<CloseIcon />}>Logout</MenuItem>
            </MenuList>
          </Menu>
        </Box>
      </Flex>
    </ChakraProvider>
  );
};

export default NavBar;
