import React, { useState, useEffect } from 'react';
import { Table, Tbody, Td, Th, Thead, Tr, Button, Modal, ModalOverlay, ModalContent, ModalHeader, ModalFooter, ModalBody, ModalCloseButton } from '@chakra-ui/react';
import axios from 'axios';
import NavBar from '../base/navbar';
import 'jspdf-autotable'; // Importing jspdf-autotable
import jsPDF from 'jspdf'; // Importing jspdf along with jspdf-autotable
import { useNavigate } from 'react-router-dom';

const HomeClient = () => {
  const [selectedData, setSelectedData] = useState({});
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [data, setData] = useState([]);
  const isLogged = sessionStorage.getItem('user') != null;
  console.log(JSON.parse(sessionStorage.getItem("user"))?.email)

  useEffect(() => {
    axios.get('http://localhost:5000/vehicules_users/' + JSON.parse(sessionStorage.getItem("user"))?.id)
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

  const downloadPDF = () => {
    const pdfDoc = new jsPDF();

    const title = `Historique du Vehicule ${selectedData.vehicule?.matricule || ''}`;
    const titleWidth = pdfDoc.getTextDimensions(title).w;
  
    const pageWidth = pdfDoc.internal.pageSize.width;
    const xPosition = (pageWidth - titleWidth) / 2; // Calculer la position pour centrer le texte horizontalement
  
    pdfDoc.text(title, xPosition, 15);
    
    const columns = ["Entry Date", "Exit Date", "Parking Duration"];
    const rows = selectedData.time_parking.map(time => [time.date_entree, time.date_sortie, time.difference]);

    pdfDoc.autoTable({
      head: [columns],
      body: rows,
      startY: 20,
    });
    pdfDoc.text('SmartParking.', pdfDoc.internal.pageSize.width / 2, pdfDoc.internal.pageSize.height - 10, 'center')
    pdfDoc.save('parking_details.pdf');
  };
  const sendToEmail = async () => {
    try {
      const subject = 'Parking Details';
  
      // Générer le PDF
      const pdfDoc = new jsPDF();
  
      const title = `Historique du Vehicule ${selectedData.vehicule?.matricule || ''}`;
      const titleWidth = pdfDoc.getTextDimensions(title).w;
  
      const pageWidth = pdfDoc.internal.pageSize.width;
      const xPosition = (pageWidth - titleWidth) / 2; // Calculer la position pour centrer le texte horizontalement
  
      pdfDoc.text(title, xPosition, 15);
  
      const columns = ["Entry Date", "Exit Date", "Parking Duration"];
      const rows = selectedData.time_parking.map(time => [time.date_entree, time.date_sortie, time.difference]);
  
      pdfDoc.autoTable({
        head: [columns],
        body: rows,
        startY: 20,
      });
      pdfDoc.text('SmartParking.', pdfDoc.internal.pageSize.width / 2, pdfDoc.internal.pageSize.height - 10, 'center');
  
      // Convertir le PDF en base64
      const pdfBase64 = pdfDoc.output('dataurlstring');
  
      // Envoyer les données au serveur avec le PDF en tant que pièce jointe
      const response = await axios.post('http://localhost:3001/send-email', {
        to: JSON.parse(sessionStorage.getItem("user"))?.email,
        subject,
        pdfAttachment: pdfBase64,
      });
  
      console.log(response.data.message); // Afficher le message du serveur
    } catch (error) {
      console.error('Error sending e-mail:', error);
    }
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
              <Tr key={element.vehicule.id}>
                <Td textAlign="center">{element.vehicule?.matricule}</Td>
                <Td textAlign="center">{element.vehicule?.abonnement_id}</Td>
                <Td textAlign="center">{element.abonnement.duree }</Td>
                <Td textAlign="center">
                  <Button onClick={() => openModal(element)}>Show Details</Button>
                </Td>
              </Tr>
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
                    <Tr key={time.date_entree}>
                      <Td textAlign="center">{time.date_entree}</Td>
                      <Td textAlign="center">{time.date_sortie}</Td>
                      <Td textAlign="center">{time.difference}</Td>
                    </Tr>
                  ))}
                </Tbody>
              </Table>}
            </ModalBody>
            <ModalFooter>
              <Button onClick={downloadPDF}>Download PDF</Button>
              <Button ml={3} onClick={sendToEmail}>Send to Email</Button>
            </ModalFooter>
          </ModalContent>
        </Modal>
      </div>
    </div>
  );
};

export default HomeClient;
