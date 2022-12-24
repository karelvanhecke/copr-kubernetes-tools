%global goipath helm.sh/helm/v3
%global forgeurl https://github.com/helm/helm
Version: 3.10.3

%global gomodulesmode GO111MODULE=on

%gometa

%global commit0 835b7334cfe2e5e27870ab3ed4135f136eecc704
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
-X helm.sh/helm/v3/internal/version.metadata=%{version} \
-X helm.sh/helm/v3/internal/version.gitCommit=%{commit0} \
-X helm.sh/helm/v3/internal/version.gitTreeState=clean "
%gobuild -o %{gobuilddir}/bin/helm %{goipath}/cmd/helm

%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc CONTRIBUTING.md OWNERS README.md SECURITY.md ADOPTERS.md code-of-conduct.md
%{_bindir}/*

%changelog
* Sat Dec 24 2022 Karel Van Hecke <copr@karelvanhecke.com> - 3.10.3-1
- Initial build
