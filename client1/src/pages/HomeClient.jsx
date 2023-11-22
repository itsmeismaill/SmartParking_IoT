// HomeClient.js
import React, { useState, useEffect } from 'react';
import { Table, Tbody, Td, Th, Thead, Tr, Button, Modal, ModalOverlay, ModalContent, ModalHeader, ModalFooter, ModalBody, ModalCloseButton } from '@chakra-ui/react';
import axios from 'axios';
import NavBar from '../base/navbar';
import { useNavigate } from 'react-router-dom';

const HomeClient = () => {
  const [selectedData, setSelectedData] = useState({});
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [data, setData] = useState([]);
  const isLogged = sessionStorage.getItem('user')!=null

  useEffect(() => {
    axios.get('http://localhost:5000/vehicules_users/'+JSON.parse(sessionStorage.getItem("user"))?.id) 
      .then(response => {
        console.log(response);
    
        setData(response.data.map(entry => entry) || [])
      })
      .catch(error => console.error('Erreur de récupération des véhicules', error));
  }, []);

  const openModal = (data) => {
    setSelectedData(data);
    setIsModalOpen(true);
  };

  const closeModal = () => {
    setSelectedData(null);
    setIsModalOpen(false);
  };

  return (
    <div > 
         <NavBar />
    <div style={{ marginTop: '100px' }}>
      <Table variant="simple">
        <Thead>
          <Tr>
            <Th textAlign="center">Matricule</Th>
            <Th textAlign="center">Abonnement ID</Th>
            <Th textAlign="center">Durée de l'abonnement</Th>
            <Th textAlign="center">Action</Th>
          </Tr>
        </Thead>
        <Tbody>
          {Array.isArray(data) && data.map(element => (
            <>
            <Tr key={element.vehicule.id}>
              <Td textAlign="center">{element.vehicule?.matricule}</Td>
              <Td textAlign="center">{element.vehicule?.abonnement_id}</Td>
              <Td textAlign="center">{element.abonnement.duree || ''}</Td>
              <Td textAlign="center">
                <Button onClick={() => openModal(element)}>Show Details</Button>
              </Td>
            </Tr>
    </>
          ))}
        </Tbody>
      </Table>
      {/* Modal for showing details */}
      <Modal isOpen={isModalOpen} onClose={closeModal}>
      <ModalOverlay />
      <ModalContent style={{ width: "100%", maxWidth: "900px" }}>
        <ModalHeader>Details</ModalHeader>
        <ModalCloseButton />
        <ModalBody>
          {/* Display details of selectedVehicule here */}
         
         {selectedData && <Table variant="simple">
         <Thead>
           <Tr>
             <Th textAlign="center">Entry Date</Th>
             <Th textAlign="center">Exit Date</Th>
             <Th textAlign="center">Parking Duration</Th>
           </Tr>
         </Thead>
         <Tbody>
           {Array.isArray(selectedData.time_parking) && selectedData.time_parking.map(time => (
             <Tr>
               <Td textAlign="center">{time.date_entree}</Td>
               <Td textAlign="center">{time.date_sortie}</Td>
               <Td textAlign="center">{time.difference}</Td>
             </Tr>
           ))}
         </Tbody>
       </Table>}
        </ModalBody>
        <ModalFooter>
          <Button onClick={closeModal}>Close</Button>
        </ModalFooter>
      </ModalContent>
    </Modal>
 
      </div>
    </div>
  );
};

export default HomeClient;