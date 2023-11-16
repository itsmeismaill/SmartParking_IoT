
import React from 'react'

import {
  Flex,
  Container,
  Heading,
  Stack,
  Text,
  Button,
  Icon,
  IconProps,
} from '@chakra-ui/react'
import { Link } from 'react-router-dom'
import image from '../img/NewIllustration.jpg'

/**
 * @param {IconProps} props
 */


const  Landing=()=> {
  return (
    <Container maxW={'5xl'}>
      <Stack
        textAlign={'center'}
        align={'center'}
        spacing={{ base: 8, md: 10 }}
        py={{ base: 20, md: 28 }}>
        <Heading
          fontWeight={600}
          fontSize={{ base: '3xl', sm: '4xl', md: '6xl' }}
          lineHeight={'110%'}>
          Welcome to your{' '}
          <Text as={'span'} color={'blue.400'}>
            Smart Parking
          </Text>
        </Heading>
        <Text color={'gray.500'} maxW={'3xl'}>
        Bienvenue sur Smart Parking, votre destination en ligne pour simplifier votre expérience de stationnement. Avec notre site web convivial, vous pouvez désormais souscrire à des abonnements de stationnement en toute simplicité, vous offrant une solution pratique et sans tracas pour garantir votre place de parking.
        </Text>
        <Stack spacing={6} direction={'row'}>
            <Link to="/Authentification">
          <Button
            rounded={'full'}
            px={6}
            colorScheme={'blue'}
            bg={'blue.400'}
            _hover={{ bg: 'blue.500' }}>
            
            Get started
          </Button>
          </Link>
          <Button rounded={'full'} px={6}>
            Learn more
          </Button>
        </Stack>
        <Flex w={'full'} height={'570px'}>
          <img src={image}  />
        </Flex>
      </Stack>
    </Container>
  )
}
export default Landing;