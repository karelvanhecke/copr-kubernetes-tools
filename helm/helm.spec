%global goipath helm.sh/helm/v3
%global forgeurl https://github.com/helm/helm
Version: 3.11.1

%global gomodulesmode GO111MODULE=on

%gometa

%global commit0 293b50c65d4d56187cd4e2f390f0ada46b4c4737
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: helm
Release: 1%{?dist}
Summary: The Kubernetes Package Manager
License: Apache-2.0
URL: %{gourl}
Source0: %{gosource}

%description
%{summary}

%prep
%goprep -k

%build
export LDFLAGS="-X helm.sh/helm/v3/internal/version.version=%{version} \
-X helm.sh/helm/v3/internal/version.gitCommit=%{commit0} \
-X helm.sh/helm/v3/internal/version.gitTreeState=archive "
%gobuild -o %{gobuilddir}/bin/helm %{goipath}/cmd/helm

%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc CONTRIBUTING.md OWNERS README.md SECURITY.md ADOPTERS.md code-of-conduct.md
%{_bindir}/*

%changelog
* Fri Feb 10 2023 Karel Van Hecke <copr@karelvanhecke.com> - 3.11.1-1
- Bump to 3.11.1 - security release
* Thu Jan 19 2023 Karel Van Hecke <copr@karelvanhecke.com> - 3.11.0-1
- Bump to 3.11.0
* Sat Dec 24 2022 Karel Van Hecke <copr@karelvanhecke.com> - 3.10.3-2
- Fix version
* Sat Dec 24 2022 Karel Van Hecke <copr@karelvanhecke.com> - 3.10.3-1
- Initial build
