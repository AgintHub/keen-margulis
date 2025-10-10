from typing import List


def save_images_to_storage(image_data: str, output_directory: str, file_format: str) -> List[str]:
    """
    Saves image data to storage, returning a list of saved file paths.

    Parameters
    ----------
    image_data : str
        The image data to be saved, expected to be in bytes format but
        passed as str
    output_directory : str
        The directory path where images will be saved
    file_format : str
        The file format for the images (e.g., 'jpg', 'png')

    Returns
    -------
    List[str]
        A list of file paths where the images were saved

    Raises
    ------
    ValueError
        If the output directory is invalid or inaccessible
    TypeError
        If image_data is not of type str or if output_directory or
        file_format are not strings

    Examples
    --------
    >>> save_images_to_storage(image_data='image1_bytes',
    output_directory='/tmp/images', file_format='jpg')
    >>> save_images_to_storage(image_data='image2_bytes',
    output_directory='/tmp/images', file_format='png')
    ['/tmp/images/image1.jpg', '/tmp/images/image2.png']

    >>> save_images_to_storage(image_data=['image_bytes1', 'image_bytes2'],
    output_directory='/tmp/images', file_format='jpg')
    ['/tmp/images/image1.jpg', '/tmp/images/image2.jpg']

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")