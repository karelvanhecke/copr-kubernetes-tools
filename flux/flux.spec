%global goipath github.com/fluxcd/flux2
Version: 0.40.2

%global gomodulesmode GO111MODULE=on

%gometa

Name: flux
Release: 1%{?dist}
Summary: Open and extensible continuous delivery solution for Kubernetes. Powered by GitOps Toolkit.
License: Apache-2.0
URL: %{gourl}
Source0: %{gosource}

BuildRequires: kustomize
BuildRequires: make

%description
%{summary}

%prep
%goprep -k

%build
export EMBEDDED_MANIFESTS_TARGET=cmd/flux/.manifests.done
make $EMBEDDED_MANIFESTS_TARGET
export LDFLAGS="-X main.VERSION=%{version} "
%gobuild -o %{gobuilddir}/bin/flux %{goipath}/cmd/flux

%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%files
%license LICENSE
%{_bindir}/*

%changelog
* Fri Feb 03 2023 Karel Van Hecke <copr@karelvanhecke.com> - 0.40.2-1
- Bump to 0.40.2
* Fri Feb 03 2023 Karel Van Hecke <copr@karelvanhecke.com> - 0.39.0-1
- Bump to 0.39.0
* Thu Jan 12 2023 Karel Van Hecke <copr@karelvanhecke.com> - 0.38.3-1
- Bump to 0.38.3
* Sat Dec 24 2022 Karel Van Hecke <copr@karelvanhecke.com> - 0.38.2-1
- Initial build
