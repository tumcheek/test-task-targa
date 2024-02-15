import { useState } from 'react';
import FileUpdateForm from './FileUpdateForm';

export default FileContent;

function FileContent({ fileData, currentPath }) {
    const [isFileUpdating, setIsFileUpdating] = useState(false);
  
    return (
        <div className="file">
            {isFileUpdating
                ? <FileUpdateForm fileData={fileData} currentPath={currentPath} onUpdate={onUpdate}/>
                : <div className="file_content">
                    <div className="file_content_body">{fileData.content}</div>
                    <button className="file_content_update-btn" onClick={() => setIsFileUpdating(true)}>Update</button>
                </div>
            }
        </div>
    );

    function onUpdate(newContent) {;
        fileData.content = newContent;
        setIsFileUpdating(false)
    }
}