%define debug_package %{nil}

%{!?luaver: %global luaver %(lua -e "print(string.sub(_VERSION, 5))")}
# for arch-independent modules
%global luapkgdir %{_datadir}/lua/%{luaver}

%define vermagic1 2.0.rc11
%define vermagic2 0

Name:           busted
Version:        %{vermagic1}_%{vermagic2}
Release:        2%{?dist}
Summary:        Lua unit testing framework

License:        MIT
URL:            https://github.com/Olivine-Labs/busted
Source0:        https://github.com/Olivine-Labs/busted/archive/v2.0.rc11-0.tar.gz

BuildArch:      noarch
BuildRequires:  lua-devel >= %{luaver}
%if 0%{?rhel} == 6
Requires:       lua >= %{luaver}
Requires:       lua < 5.2
%else
Requires:       lua(abi) >= %{luaver}
%endif

Requires:       lua-penlight
Requires:       lua-term
Requires:       lua-dkjson
Requires:       lua-socket
Requires:       lua-cliargs
Requires:       lua-say
Requires:       lua-filesystem
Requires:       lua-luassert
Requires:       lua-mediator
Requires:       luacov

%description
An elegant, extensible, testing framework. Ships with a large amount of useful
asserts, plus the ability to write your own. Output in pretty or plain terminal
format, JSON, or TAP for CI integration. Great for TDD and unit, integration,
and functional tests.


%prep
%setup -q -n busted-%{vermagic1}-%{vermagic2}


%build


%install
install -d %{buildroot}%{luapkgdir}
cp -ar busted %{buildroot}%{luapkgdir}
install -p -m755 -D bin/busted %{buildroot}%{_bindir}/busted

# completions for bash and zsh
install -p -m644 -D completions/bash/busted.bash \
	%{buildroot}%{_datadir}/bash-completion/completions/busted
install -p -m644 -D completions/zsh/_busted \
	%{buildroot}%{_datadir}/zsh/site-functions/_busted


%files
%license LICENSE
%doc CONTRIBUTING.md README.md TODO.md
%{_bindir}/busted
%{luapkgdir}/busted/
%{_datadir}/bash-completion/
%{_datadir}/zsh/


%changelog
* Thu May 19 2016 Jajauma's Packages <jajauma@yandex.ru> - 2.0.rc11_0-2
- Require luacov

* Thu May 19 2016 Jajauma's Packages <jajauma@yandex.ru> - 2.0.rc11_0-1
- Public release
