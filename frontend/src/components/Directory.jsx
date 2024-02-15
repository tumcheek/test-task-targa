import { deleteEntity, entityLink, formatDate } from '../helpers/utils.js';
export default Directory;

function Directory({ dirName, dirInfo, currentPath, onDelete }) {
    const deleteDirectory = () => deleteEntity(dirName, { type: 'directory', currentPath, onDelete });
    const dirLink = entityLink(dirName, { currentPath });

    return (
        <div className="directory_item directory">
            <a href={dirLink} className="directory_item_link far fa-folder">{dirName}</a>
            <span>{dirInfo.size}</span>
            <span className="directory_item_data date">{formatDate(dirInfo.created_at)}</span>
            <span className="directory_item_data date">{formatDate(dirInfo.updated_at)}</span>
            <span className="directory_item_delete-btn far fa-trash-alt" onClick={deleteDirectory}></span>
        </div>
    );
}