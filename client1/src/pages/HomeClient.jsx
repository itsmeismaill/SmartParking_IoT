// HomeClient.js
import React, { useState, useEffect } from 'react';
import { Table, Tbody, Td, Th, Thead, Tr, Button, Modal, ModalOverlay, ModalContent, ModalHeader, ModalFooter, ModalBody, ModalCloseButton } from '@chakra-ui/react';
import axios from 'axios';
import NavBar from '../base/navbar';

const HomeClient = () => {
  const [vehicules, setVehicules] = useState([]);
  const [abonnements, setAbonnements] = useState([]);
  const [selectedVehicule, setSelectedVehicule] = useState(null);
  const [isModalOpen, setIsModalOpen] = useState(false);

  useEffect(() => {
    axios.get('http://localhost:5000/vehicules_users/', { withCredentials: true }) 
      .then(response => {
        console.log(response); // Log the entire response
        // Assuming response.data is an array of objects with 'abonnement' and 'vehicule' properties
        setVehicules(response.data.map(entry => entry.vehicule) || []);
        setAbonnements(response.data.map(entry => entry.abonnement) || []);
      })
      .catch(error => console.error('Erreur de récupération des véhicules', error));
  }, []);

  const openModal = (vehicule) => {
    setSelectedVehicule(vehicule);
    setIsModalOpen(true);
  };

  const closeModal = () => {
    setSelectedVehicule(null);
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
          {Array.isArray(vehicules) && vehicules.map(vehicule => (
            <Tr key={vehicule.id}>
              <Td textAlign="center">{vehicule?.matricule}</Td>
              <Td textAlign="center">{vehicule?.abonnement_id}</Td>
              <Td textAlign="center">{abonnements.find(abonnement => abonnement.id === vehicule?.abonnement_id)?.duree || ''}</Td>
              <Td textAlign="center">
                <Button onClick={() => openModal(vehicule)}>Show Details</Button>
              </Td>
            </Tr>
          ))}
        </Tbody>
      </Table>

      {/* Modal for showing details */}
      <Modal isOpen={isModalOpen} onClose={closeModal}>
        <ModalOverlay />
        <ModalContent>
          <ModalHeader>Details</ModalHeader>
          <ModalCloseButton />
          <ModalBody>
            {/* Display details of selectedVehicule here */}
            {selectedVehicule && (
              <div>
                <p>Matricule: {selectedVehicule.matricule}</p>
                <p>Abonnement ID: {selectedVehicule.abonnement_id}</p>
                <p>Durée de l'abonnement: {selectedVehicule.abonnement ? selectedVehicule.abonnement.duree : ''}</p>
              </div>
            )}
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