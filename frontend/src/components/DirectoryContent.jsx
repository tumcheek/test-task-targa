import File from "./File.jsx";
import Directory from "./Directory.jsx";

export default DirectoryContent;

function DirectoryContent({ dirData, currentPath, onDelete }){
    const labels = ['Name', 'Size', 'Created At', 'Updated At'];
    const headings = labels.map(label => (
        <div key={label}>{label}</div>)
    );
    const files = dirData.files?.map(([fileName, fileInfo]) => (
        <File currentPath={currentPath} fileInfo={fileInfo} fileName={fileName} onDelete={onDelete} key={fileName} />
    ));
    const directories = dirData.directories?.map(([dirName, dirInfo]) => (
        <Directory currentPath={currentPath} dirInfo={dirInfo} dirName={dirName} onDelete={onDelete} key={dirName} />
    ));

    return (
        <div className="directory_content">
            <div className="directory_head">
                {headings}    
            </div>
            <div className="directory_items">
                {files}
                {directories}
            </div>
        </div>
    );
}