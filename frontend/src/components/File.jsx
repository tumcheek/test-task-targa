import { deleteEntity, entityLink, formatDate } from '../helpers/utils.js';

export default File;

function File({ fileName, fileInfo, currentPath, onDelete }) {
    const deleteFile = () => deleteEntity(fileName, { type: 'file', currentPath, onDelete });
    const fileLink = entityLink(fileName, { type: 'file', currentPath });

    return (
        <div className="directory_item file">
            <a href={fileLink} className="directory_item_link far fa-file">{fileName}</a>
            <span>{fileInfo.size}</span>
            <span className="directory_item_data date">{formatDate(fileInfo.created_at)}</span>
            <span className="directory_item_data date">{formatDate(fileInfo.updated_at)}</span>
            <span className="directory_item_delete-btn far fa-trash-alt" onClick={deleteFile}></span>
        </div>
    );
}