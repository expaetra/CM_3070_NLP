//Handle all communication between frontend and backend
//Contains all FETCH logic
const API = "http://127.0.0.1:8000";

// Fetch the list of uplaoded PDFs 
export async function fetchDocuments(){
  const res = await fetch(`${API}/documents`);
  const data = await res.json();
  return data.documents || []; //Return document array
} 

//Upload one or multiple PDF files to backend
export async function uploadDocuments(files) {
  const formData = new FormData(); 

  //Append all selected files to the form data:
  for (const file of files) {
    formData.append("files", file);
  } 

  //Send them to the /upload endpoint
  await fetch(`${API}/upload`, {
    method: "POST",
    body: formData,
  });
}

//Fetch one documents extracted data (Abstract & prediction)
export async function fetchDocument(name) {
  const res = await fetch(
    `${API}/document/${encodeURIComponent(name)}`
  );

  //Return JSON repsonse from the backend
  return await res.json();
}
