import React, { useState } from 'react';
import {
  Flex,
  Box,
  FormControl,
  FormLabel,
  Input,
  InputGroup,
  HStack,
  InputRightElement,
  Stack,
  Button,
  Heading,
  Text,
  useColorModeValue,
  Link,
} from '@chakra-ui/react';
import { ViewIcon, ViewOffIcon } from '@chakra-ui/icons';

const SignUp = () => {
  const [showPassword, setShowPassword] = useState(false);
  const [formData, setFormData] = useState({
    id:'2',
    username: '',
    cin: '',
    telephone: '',
    email: '',
    password: '',
    role:'client'
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.id]: e.target.value,
    });
  };

  const handleSubmit = async () => {
    try {
        console.log("button clickee");
      const response = await fetch('http://localhost:5000/users', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            id: formData.id,
            username: formData.username,
            cin: formData.cin,
            telephone: formData.telephone,
            email: formData.email,
            password: formData.password,
            role: formData.role,
          }),
      });

      if (response.ok) {
        const userData = await response.json();
        console.log('User added:', userData);
        // Perform any additional actions on success
      } else {
        console.error('Error adding user:', response.statusText);
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
          <Heading fontSize={'4xl'} textAlign={'center'}>
            Sign up
          </Heading>
        </Stack>
        <Box
          rounded={'lg'}
          bg={useColorModeValue('white', 'gray.700')}
          boxShadow={'lg'}
          p={8}>
          <Stack spacing={4}>
          <HStack spacing={4}>
              <FormControl id="username" isRequired>
                <FormLabel>Username</FormLabel>
                <Input type="text"
                     value={formData.username}
                     onChange={(e) => handleChange(e, 'username')} />
              </FormControl>
              <FormControl id="cin" isRequired>
                <FormLabel>CIN</FormLabel>
                <Input type="text"
                     value={formData.cin}
                     onChange={(e) => handleChange(e, 'cin')} />
              </FormControl>
            </HStack>
            <HStack spacing={4}>
              <FormControl id="telephone" isRequired>
                <FormLabel>Telephone</FormLabel>
                <Input type="tel" 
                    value={formData.telephone}
                    onChange={(e) => handleChange(e, 'telephone')} />
              </FormControl>
              <FormControl id="email" isRequired>
                <FormLabel>Email address</FormLabel>
                <Input type="email" 
                       value={formData.email}
                      onChange={(e) => handleChange(e, 'email')} />
              </FormControl>
            </HStack>
            <FormControl id="password" isRequired>
              <FormLabel>Password</FormLabel>
              <InputGroup>
                <Input type={showPassword ? 'text' : 'password'}
                     value={formData.password}
                     onChange={(e) => handleChange(e, 'password')} /> 
                <InputRightElement h={'full'}>
                  <Button
                    variant={'ghost'}
                    onClick={() => setShowPassword((showPassword) => !showPassword)}>
                    {showPassword ? <ViewIcon /> : <ViewOffIcon />}
                  </Button>
                </InputRightElement>
              </InputGroup>
            </FormControl>
            <Stack spacing={10} pt={2}>
              <Button
                loadingText="Submitting"
                size="lg"
                bg={'blue.400'}
                color={'white'}
                onClick={handleSubmit}
                _hover={{
                  bg: 'blue.500',
                }}>
                Sign up
              </Button>
            </Stack>
            <Stack pt={6}>
              <Text align={'center'}>
                Already a user? <Link color={'blue.400'}>Login</Link>
              </Text>
            </Stack>
          </Stack>
        </Box>
      </Stack>
    </Flex>
  );
};

export default SignUp;

