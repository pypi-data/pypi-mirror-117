GalleryWidget
===============

.. _widget_docs:

The ``GalleryWidget`` class
----------------------------

.. autoclass:: galleryfield.widgets.GalleryWidget

.. note:: When a :class:`galleryfield.fields.GalleryField` instance is initialized
   with ``galleryfield.BuiltInGalleryImage``, the widget instance will
   automatically use URL names ``builtingalleryimage-upload``
   ``builtingalleryimage-fetch`` and ``builtingalleryimage-crop`` for
   :attr:`upload_url`, :attr:`fetch_url` and :attr:`crop_request_url`,
   respectively.

The url params can be assigned after the formfield is initialized. For example:

.. code-block:: python

    class MyGalleryForm(forms.ModelForm):
        class Meta:
            model = MyGallery
            fields = ["images"]

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields["images"].widget.upload_url = "my-upload-handler"

The validity of the url params will be checked during rendering.

.. warning:: You NEED to make sure all the urls in the widget are
   handling the corresponding :attr:`target_model` before put into
   production. As a minimal precaution,
   when a :class:`galleryfield.fields.GalleryField` instance (
   or a :class:`galleryfield.fields.GalleryFormField` instance, or image handling views
   ) is
   **NOT** initialized with ``galleryfield.BuiltInGalleryImage`` as the
   :attr:`target_model`, assigning built-in urls (
   i.e., ``builtingalleryimage-upload``, ``builtingalleryimage-fetch``)
   in widget params, or set ``builtingalleryimage-crop`` for `crop_url_name` in
   image handling views, :exc:`ImproperlyConfigured` will be raised
   when rendering. The reason is, those built-in views are handling
   built-in :class:`galleryfield.models.BuiltInGalleryImage` instances.
