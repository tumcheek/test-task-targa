import {useEffect, useState} from "react";
import {useSearchParams} from "react-router-dom";
import DirectoryContent from "./DirectoryContent.jsx";
import FileContent from "./FileContent.jsx";
import FileCreationForm from "./FileCreationForm.jsx";
import DirectoryCreationForm from "./DirectoryCreationForm.jsx";
import SearchForm from "./SearchForm.jsx";
import * as config from '../helpers/config.js';

export default Filesystem;

function Filesystem () {
    const [searchParams] = useSearchParams();
    const currentPath = searchParams.get('path');
    const is_file = searchParams.get('is_file');
    const [dirData, setDirData] = useState(null);

    useEffect(fetchStructure, [searchParams]);

    if(!dirData) return null;

    return (
        <div className='filesystem'>
            <SearchForm onSearch={updateFilesystem} />
            {is_file 
                ? <FileContent currentPath={currentPath} fileData={dirData}/>
                : <>
                    <DirectoryContent dirData={dirData} currentPath={currentPath} onDelete={updateFilesystem}/>
                    <div className='filesystem_actions'>
                        <DirectoryCreationForm currentPath={currentPath} onCreate={updateFilesystem} />
                        <FileCreationForm currentPath={currentPath} onCreate={updateFilesystem} />
                    </div>
                </>}
        </div>
    );

    function fetchStructure() {
        const pathUrl = new URL(config.url.root);

        if (currentPath) {
            pathUrl.searchParams.set('path', currentPath);
            is_file && pathUrl.searchParams.set('is_file', true);
        }

        fetch(pathUrl)
            .then(response => response.json())
            .then(result => setDirData(result))
            .catch(console.error);
    }

    function updateFilesystem(structure) {
        setDirData(structure)
    }
}

