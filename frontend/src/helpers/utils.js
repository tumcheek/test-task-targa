import * as config from '../helpers/config.js';

export { 
    deleteEntity,
    entityLink,
    entityPath,
    formatDate
};

const apiUrls = {
    file: config.url.files,
    directory: config.url.directories,
};

function deleteEntity(name, { type, currentPath, onDelete }) {
    const actionUrl = new URL(apiUrls[type]);

    currentPath && actionUrl.searchParams.set('path', currentPath);
    actionUrl.pathname += name;
    fetch(actionUrl, { method: 'DELETE' })
        .then(response => response.json(), console.log)
        .then(onDelete);
}

function entityLink(name, { type, currentPath }) {
    const typeParamKey = {
        file: 'is_file'
    };
    const path = currentPath ? `${currentPath}/${name}` : name;
    const typeFlag = type in typeParamKey ? `&${typeParamKey[type]}=true` : '';

    return `?path=${path}${typeFlag}`;
}

function entityPath(name, { type, currentPath }) {
    const pathSeparator = '/';
    const actionUrl = new URL(apiUrls[type]);

    actionUrl.pathname += name;

    if (currentPath) {
        const pathParam = currentPath.split(pathSeparator).toSpliced(-1).join(pathSeparator);
        pathParam && actionUrl.searchParams.set('path', pathParam);
    }

    return actionUrl;
}

function formatDate(dateString) {
    const options = {
        year: 'numeric',
        month: 'numeric',
        day: 'numeric',
        hour: 'numeric',
        minute: 'numeric',
        second: 'numeric',
        hour12: false
    };

    return (new Date(dateString)).toLocaleString(undefined, options);
}