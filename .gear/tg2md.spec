Name: python3-module-tg2md
Version: 0.1
Release: alt1
Summary: Parser output from Telegram channel to jelly-applicable post in markdown
License: BSD 3-Clause License
Group: Development/Python3

BuildArch: noarch

Url: https://github.com/la-ninpre/tg2md

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-module-setuptools
BuildRequires: python3-module-wheel

%description
This script parses output from Telegram channel and converts each post to jekyll-applicable post in markdown.
Telegram Desktop creates JSON file, as well as different directories containing multimedia, photos, etc.
This script creates new directory and populates it with formatted posts ready to publish.

%prep
%setup

%build
%python3_build

%install
%python_install


%files

%changelog
* Thu Oct 10 2024 Anatoly Sinelnikov <noizydwarf@gmail.com> 0.1-alt1
- Build for Sisyphus

