import React, { useState } from 'react';
import {
  Flex,
  Box,
  FormControl,
  FormLabel,
  Input,
  Checkbox,
  Stack,
  Button,
  Heading,
  Text,
  useColorModeValue,
} from '@chakra-ui/react';
import { Link, useNavigate } from 'react-router-dom'

const Authentification = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    username: '',
    password: '',
  });


  const handleChange = (e, fieldName) => {
    setFormData({
      ...formData,
      [fieldName]: e.target.value,
    });
  };


  const handleSubmit = async () => {
    try {
        console.log("button clickee");
      const response = await fetch('http://localhost:5000/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            username: formData.username,
            password: formData.password,
            
          }),
      });

      if (response.ok) {
        const userData = await response.json();
        console.log("userRole", userData.user.role);

        if(userData?.user) sessionStorage.setItem('user', JSON.stringify(userData.user));

        // Redirect to "/dashboard" if user role is "admin"
        if (userData.user.role === 'admin') {
          navigate('/dashboard')
        } else if(userData.user.role === 'client'){
          navigate('/HomeClient')
        }

      } else {
        console.error('Error connection', response.statusText);
      }
    } catch (error) {
      console.error('Error:', error.message);
    }
  };
  return (
    <Flex
      minH={'100vh'}
      align={'center'}
      justify={'center'}
      bg={useColorModeValue('gray.50', 'gray.800')}>
      <Stack spacing={8} mx={'auto'} maxW={'lg'} py={12} px={6}>
        <Stack align={'center'}>
          <Heading fontSize={'4xl'}>Sign in to your account</Heading>
        </Stack>
        <Box
          rounded={'lg'}
          bg={useColorModeValue('white', 'gray.700')}
          boxShadow={'lg'}
          p={8}>
          <Stack spacing={4}>
            <FormControl id="username">
              <FormLabel>Username</FormLabel>
              <Input
                type="text"
                value={formData.username}
                onChange={(e) => handleChange(e, 'username')}
              />
            </FormControl>
            <FormControl id="password">
              <FormLabel>Password</FormLabel>
              <Input
                type="password"
                value={formData.password}
                onChange={(e) => handleChange(e, 'password')}
              />
            </FormControl>
            <Stack spacing={10}>
              <Stack
                direction={{ base: 'column', sm: 'row' }}
                align={'start'}
                justify={'space-between'}>
                <Checkbox>Remember me</Checkbox>
                <Text color={'blue.400'}>Forgot password?</Text>
              </Stack>
              
              <Button
                bg={'blue.400'}
                color={'white'}
                onClick={handleSubmit}
                _hover={{
                  bg: 'blue.500',
                }}>
                
                Sign In
              </Button>

              <Button
                bg={'blue.400'}
                color={'white'}
                _hover={{
                  bg: 'blue.500',
                
                }}
                 onClick={()=>navigate("/SignUp")}>
                Sign Up
              </Button>

            </Stack>
          </Stack>
        </Box>
      </Stack>
    </Flex>
  );
};

export default Authentification;
