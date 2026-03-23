//Handles uploading PDF files,
//Sends the selected files back to the parent component

export default function FileUploader({ onUpload }) {
  async function handleChange(e) { //Triggered when user selects file(s)
    const files = e.target.files;
    if (!files.length) return;
    await onUpload(files); //Send file(s) to parent components
  }

  return (
    <input
      type = "file"
      accept = ".pdf" //Accept only PDF files
      multiple //Allow multiple files
      onChange={handleChange} //Handle file selection
    />
  );
}
