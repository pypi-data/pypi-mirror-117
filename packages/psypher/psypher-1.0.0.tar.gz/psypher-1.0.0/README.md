# Psypher - A modern asymmetric encryption scheme.

Psypher is a modern cryptography module providing high-level security recipes with simple interfaces. It is built for securing communication through insecure  channels.

## Installation

This module is available via PyPI:
```shell
$ pip install psypher
```

If you want to use the source code directly, make sure you install the `cryptography` dependency.

```shell
$ pip install cryptography
```

## Basic Usage

All the interface Psypher provides is accessible through the `Scheme` interface. Use the `default` static method to obtain an instance of the default scheme (`curve25519-chacha20poly1305`).
```py
>>> from psypher import Scheme
>>> s1, s2 = Scheme.default(), Scheme.default()
>>> s1.__class__.__name__
'Curve25519ChaCha20Poly1305Scheme'
```

The private and public key is accessible with the `privateKey` and `publicKey` properties. The basic usage of these keys are shown below.
```py
# key export (also suitable for public keys)
key1 = s1.privateKey.export() # bytes
key2 = s2.privateKey.exportJson() # str
# key import (also suitable for public keys)
psypher.secret.Curve25519PrivateKey.importKey(key1)
psypher.secret.Curve25519PrivateKey.importJson(key2)
# encrypted key export (private keys only)
key1 = s1.privateKey.secureExport(b'password')
key2 = s2.privateKey.secureExportJson(b'password')
# encrypted key import (private keys only)
psypher.secret.Curve25519PrivateKey.importKey(key1, b'password')
psypher.secret.Curve25519PrivateKey.importJson(key2, b'password')
# key fingerprint (public keys only)
print(s1.publicKey.digest)
```

> When using encrypted key export, the default behaviours is to derive the wrapping key from the password using `PBKDF2`. However, you can specify `derive=False` to disable this kind of behaviour and to use your material as key directly.

> `IPublicKey.digest` is a cached property, so it might not behave as you expect it to be. See the *Advanced Usage / Cache Mode* to learn more.

The `export`, `exportJson` methods is also defined on the scheme as a shortcut to the public key. Use the `receive` and `receiveJson` methods to receive remote key from peers:
```py
>>> s1.receive(s2.export())
>>> s2.receiveJson(s1.exportJson())
```

Use the `shareSecret` property to calculate the negotiated shared secret. This property is CACHED, that means it only evaluates once. For detailed information about caching, please navigate to the *Advanced Usage / Cache Mode* section.
```py
>>> s1.sharedSecret == s2.sharedSecret
True
```

To generate the digital signature of specific message, use the `sign` method. Call `verify` on the other side to verify the message. You can only verify messages signed by your peer. The signature generated is deterministic.
```py
>>> data = b'My telephone number is 123456!'
>>> signature = s1.sign(data)
>>> s2.verify(data, signature)
True
>>> s2.verify(b'My telephone number is 654321!', signature)
False
```

If you just want to check the integrity of your message therefore don't require such cryptographical strength of your signature, or if you need a shorter signature value, the `integritySign` method may suits you. It uses HMAC to sign the message, producing only 32 bytes output. Likewise, the `integrityVerify` method can be used to verify this signature:
```py
>>> data = b'My telephone number is 123456!'
>>> signature = s1.integritySign(data)
>>> s2.integrityVerify(data, signature)
True
>>> s2.integrityVerify(b'My telephone number is 654321!', signature)
False
```

To encrypt your message, use the `encrypt` method. Call `decrypt` on the other side to decrypt your message. You can only decrypt messages encrypted by your peer. The ciphertext is different each time you call `encrypt`, even if you are encrypting the same message.
```py
>>> data = b'The darkest secret lies here.'
>>> ciphertext = s2.encrypt(data)
>>> s1.decrypt(ciphertext) == data
True
>>> from psypher.errors import InvalidCiphertext
>>> try:
...     s1.decrypt(b'This is absolutely illegal')
... except InvalidCiphertext:
...     pass
```

## Advanced Usage

Below are some complicated usages of this module beyond the normal usage.

### Cache Mode

The cache mode is enabled by default, which means certain methods or property will only be calculated once and cached. Cached items includes `IPublicKey.digest` and `<KeyPairClass>.sharedSecret`. You can disable caching globally with the following statements:
```py
>>> from psypher import cache
>>> cache.setenabled(False)
```

You can access the cache object through the unbound version of the method or property. Here are some usages:
```py
# query
from psypher.secret import IPublicKey
IPublicKey.digest.fget.enabled
# partially disable
IPublicKey.digest.fget.enabled = False
EccKeyPair.sharedSecret.fget.enabled = False
# clear cache for all instances
Curve25519KeyPair.sharedSecret.fget.clearCache()
```

> If you disabled the cache globally, the `enabled` property will return `False` on every instance, even if you set it to `True`.

### Customize Scheme

The scheme object is located in the `psypher.cipher` module. A scheme is consisted of two parts - the key pair and the symmetric encryptor. You could customize these parts.

The module provides two built-in schemes: `Curve15519ChaCha20Poly1305Scheme`, which is the default, and `Secp256k1AesGcmScheme`, which is recommended to use in commercial circumstances. These schemes produces the ciphertext with similar structure:

#### Curve25519ChaCha20Poly1305

Input: plain text (X bytes)

Output:

| EphKey | HkdfSalt | AeadNonce | Ciphertext | AeadTag | Total |
|--|--|--|--|--|--|
| 32 bytes | 16 bytes | 12 bytes | X bytes | 16 bytes | 76+X bytes |

#### Secp256k1AesGcm:

Input: plain text (X bytes)

Output:

| EphKey | HkdfSalt | AeadNonce | Ciphertext | AeadTag | Total |
|--|--|--|--|--|--|
| 65 bytes | 16 bytes | 12 bytes | X bytes | 16 bytes | 109+X bytes |

These schemes can be found in the `psypher.scheme` module:
```py
>>> from psypher.scheme import Secp256k1AesGcmScheme
>>> s1 = Secp256k1AesGcmScheme.generate()
```

You can also customize the schemes:
```py
>>> from psypher.cipher import AesGcmEncryptor
>>> from psypher.secret import Curve25519KeyPair
>>> from psypher.scheme import Scheme
>>> s1 = Scheme(Curve25519KeyPair.generate(), AesGcmEncryptor)
```

To fully build your own customized scheme, you may want to inherit from the `IKeyPair` class. You must implement the `IPrivateKey` and `IPublicKey` interfaces too. The `IEncryptor` interface however, is a static interface, only containing static methods. For more details, please see the source code.

## Support & License

This module is built on the `pyca/cryptography` library. See [their Github Repository](https://github.com/pyca/cryptography).

This software is licensed under the [MIT License](https://opensource.org/licenses/MIT). For more information, see the [License Text](LICENSE).