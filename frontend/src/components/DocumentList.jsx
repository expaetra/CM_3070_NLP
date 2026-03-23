//Display the list of uploaded PDF files
//Receives the document list and currently selected document, check and notfies when a document is clicked
export default function DocumentList({documents, activeDoc, onSelect}) {
  return (
    <div className="sidebar"> 
      <h3>Documents</h3> {/*Sidebar title*/}

       {/*Display a message if no documents have been uploaded*/} 
      {documents.length === 0 && (  
        <p><em>No documents uploaded</em></p> 
      )}

    {/*Show the list of uploaded documents */}
      <ul>
        {documents.map((doc) => ( 
          <li
            key={doc} //Highlight the currently selected file
            className={doc === activeDoc ? "active" : ""} 
            onClick={() => onSelect(doc)} //Notify parent component when the file is clicked
          >
            {doc}
          </li>
        ))}
      </ul>
    </div> 
  );
}
