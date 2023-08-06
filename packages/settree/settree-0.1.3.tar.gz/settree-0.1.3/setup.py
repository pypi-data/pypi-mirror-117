import setuptools

setuptools.setup(
    name="settree",                     # This is the name of the package
    version="0.1.3",                        # The initial release version
    author="Roy Hirsch",                     # Full name of the author
    author_email='royhirsch@mail.tau.ac.il',  # Type in your E-Mail
    url='https://github.com/TAU-MLwell/Set-Tree',  # Provide either the link to your github or to your website
    description="A framework for learning tree-based models over sets",
    long_description='This is the official repository for the paper: "Trees with Attention for Set Prediction Tasks" (ICML21).\n'
                     'This repository contains a prototypical implementation of Set-Tree and GBeST (Gradient Boosted Set-Tree) algorithms.\n'
                     'In many machine learning applications, each record represents a set of items. A set is an unordered group of items,'
                     ' the number of items may differ between different sets. Problems comprised from sets of items are present in diverse fields,'
                     ' from particle physics and cosmology to statistics and computer graphics. In this work, we present a novel tree-based algorithm for processing sets.\n\n'
                     'Set-Tree model comprised from two components:\n'
                     'Set-compatible split criteria: we specifically support the family of split criteria defined by the following equation and parametrized by alpha and beta.\n'
                     'Attention-Sets: a mechanism for criteria the split criteria to subsets of the input. The attention-sets are derived from previous split-criteria and allows the model to learn more complex set-functions.\n'
                     'For more details, please refer to the official repository: https://github.com/TAU-MLwell/Set-Tree\n'
                     'Or the paper: Trees with Attention for Set Prediction Tasks, http://proceedings.mlr.press/v139/hirsch21a.html',
    long_description_content_type="text/markdown",
    # packages=setuptools.find_packages(),    # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.6',                # Minimum version requirement of the package
    # packages=setuptools.find_packages(include=['settree', 'settree.*']),
    # py_modules=["settree"],                 # Name of the python package
    package_dir={'':'settree'},     # Directory of the source code of the package
    install_requires=['numpy>=1.19.2', 'scikit-learn >= 0.23.1', 'scipy >= 1.5.2']
    
    

)
