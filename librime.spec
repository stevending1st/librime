Name:           librime
Version:        1.10.0
Release:        1%{?dist}
Summary:        Rime Input Method Engine, the core library

License:        The 3-Clause BSD License
URL:            https://github.com/rime/%{name}
Source0:        https://github.com/rime/%{name}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  gcc >= 8.1
BuildRequires:  cmake >= 3.12
BuildRequires:  libboost >= 1.74
BuildRequires:  libglog
BuildRequires:  libleveldb
BuildRequires:  libmarisa
BuildRequires:  libopencc >= 1.0.2
BuildRequires:  libyaml-cpp >= 0.5
BuildRequires:  libgtest

Requires:  gcc >= 8.1
Requires:  libboost
Requires:  libglog
Requires:  libleveldb
Requires:  libmarisa
Requires:  libopencc
Requires:  libyaml-cpp

%description
Rime with your keystrokes.

%prep
%autosetup

%build
make

%install
mkdir -p %{buildroot}%{_bindir}
make install BINDIR=%{buildroot}%{_bindir} MANDIR=%{buildroot}%{_mandir}

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%license COPYING

%changelog
* Tue Feb. 9th 2024 居戎氏 <chen.sst@gmail.com> - 1.10.0
- Bug Fixes
  - chord_composer: stop at super and caps by default (8709a7a)
  - path: convert to native encoding on Windows (#806) (6546689), closes #804 rime/weasel#576 rime/weasel#1080
  - don't compress the token during collecting dict entries (#762) (#768) (767ebad)
- Features
  - api: highlight_candidate*, change_page (142902d), closes #620
  - engine: translate zero-length prediction (8f2e8d6)
  - key_binder: add when: predicting condition (#751) (3bc65c9)
  - rime_api: add RimeApi::set_input (#771) (de12d6a), closes #547
  - add reload command for rime_api_console (#741) (9b2689b)
- Performance Improvements
  - less nest in filesystem iteration When CleanOldLogFiles::Run (#801) (9ec1711)
- BREAKING CHANGES
  - path: Most string filenames in APIs are changed to path; installation.yaml should be UTF-8 encoded.
