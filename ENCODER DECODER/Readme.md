# Encoder-Decoder

**Python GUI Encryption and Decryption Project**

This Python-based GUI Encryption and Decryption project offers a user-friendly interface for securing sensitive information through text and image encryption. The application utilizes the powerful Tkinter library for creating an interactive graphical user interface, making it easy for users to encrypt and decrypt their data effortlessly.

**Features:**
1. **Text Encryption and Decryption:** The project supports the encryption and decryption of text using the Caesar cipher algorithm. The user can input any text, and the application will encrypt it with a specified key, making it unreadable to unauthorized users. Decryption can be done with the same key, revealing the original text.

2. **Image Encryption and Decryption:** The project also provides the capability to encrypt text into images using the stegano library. Users can select an image and input the text they want to hide within it. The application then conceals the text within the image, making it appear unchanged to the naked eye. Decryption retrieves the hidden text from the encrypted image.

**Libraries Used:**
- Tkinter: The standard Python GUI toolkit used for building the graphical user interface.
- cProfile: A module for profiling the application's performance and identifying bottlenecks.
- cgitb: A module for displaying detailed traceback messages in case of exceptions.
- datetime: A library for working with dates and times, useful for timestamps and time-related operations.
- PIL (Python Imaging Library): A powerful library for image processing and manipulation.
- stegano: A library for steganography, allowing the hiding of information within images.
- numpy: A popular library for numerical computing, used in this project for various image processing tasks.

**Encryption Method:**
- Caesar Cipher: A simple substitution cipher that shifts characters by a fixed key. It provides basic text encryption and decryption capabilities.

**How to Use:**
1. Input Text Encryption: Enter the text you want to encrypt, along with the encryption key, and click the "Encrypt Text" button.
2. Image Encryption: Select an image and input the text you want to hide within it, then click the "Encrypt Image" button.
3. Image Decryption: To retrieve hidden text from an encrypted image, click the "Decrypt Image" button after selecting the appropriate image.

**Note:**
The Caesar cipher is used in this project for demonstration purposes. It is not recommended for serious encryption needs. For real-world applications, use more secure encryption algorithms such as AES.

Feel free to explore, contribute, and enhance this Python-based GUI Encryption and Decryption project. Your valuable feedback and suggestions are always welcome!
