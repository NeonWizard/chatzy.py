import setuptools

with open('README.md') as f:
	readme = f.read()

with open('LICENSE') as f:
	license = f.read()

requirements = []
with open('requirements.txt') as f:
	requirements = f.read().splitlines()

setuptools.setup(
	name='chatzy.py',
	version='0.0.1',
	description='A chatzy interface in Python',
	long_description=readme,
	long_description_content_type="text/markdown",
	author='Spooky',
	author_email='contact@wizardlywonders.xyz',
	url='https://github.com/NeonWizard/chatzy.py',
	license=license,
	packages=setuptools.find_packages(exclude=('tests', 'docs')),
	install_requires=requirements,
	python_requires='>=3'
)
